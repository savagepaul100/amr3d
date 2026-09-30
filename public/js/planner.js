/**
 * EDGE-AI DECENTRALIZED MULTI-AGENT PLANNER & HIGHWAY PROTOCOL
 * 
 * Strict "Highway + Single-Driveway" Discipline:
 * 1. Cell Classification: HIGHWAY, BUFFER_<id>, ALLEY, TERMINAL_BUFFER, RACK/OBSTACLE
 * 2. Movement Rules: Free travel only on HIGHWAY; single-cell approach; mandatory reverse-out.
 * 3. Alley Rules: Rear-entry only; mutual exclusion; mandatory reverse-out.
 * 4. Decentralized Local Reservation: P2P cell claim tokens; queue at highway waiting spot; 
 *    reversing AMR has absolute exit priority over entering AMR.
 * 5. Queuing & Timeout Recovery: Replanning on highway after timeout.
 */

const CELL_TYPE = {
  EMPTY: 0,
  HIGHWAY: 1,
  RACK: 2,
  BUFFER: 3,
  ALLEY: 4,
  TERMINAL_BUFFER: 5,
  OBSTACLE: 6,
  WAITING_SPOT: 7
};

class DecentralizedPlanner {
  constructor(width = 80, height = 50) {
    this.width = width;
    this.height = height;
    
    // Grid classification map
    this.grid = new Array(width).fill(0).map(() => new Array(height).fill(CELL_TYPE.HIGHWAY));
    this.cellLabels = new Map(); // key "x,y" => { type, targetId, waitingSpot: {x,y}, alleyId }
    
    // Decentralized Claim Table (P2P Mesh Token Table)
    // key "x,y" or "alley_<id>" => { robotId, claimTime, expiresAt, status: 'RESERVED'|'OCCUPIED'|'REVERSING' }
    this.claimTable = new Map();
    
    // Reservation timeout in milliseconds
    this.CLAIM_TIMEOUT_MS = 10000;
  }

  /**
   * Set cell classification
   */
  classifyCell(x, y, type, targetId = null, waitingSpot = null, alleyId = null) {
    if (x < 0 || x >= this.width || y < 0 || y >= this.height) return;
    this.grid[x][y] = type;
    this.cellLabels.set(`${x},${y}`, {
      type,
      targetId,
      waitingSpot,
      alleyId
    });
  }

  getCellInfo(x, y) {
    return this.cellLabels.get(`${x},${y}`) || { type: this.grid[x][y] || CELL_TYPE.HIGHWAY };
  }

  /**
   * Decentralized Token Claim: Request reservation for a buffer cell or alley.
   * Reversing robots always take absolute priority.
   */
  claimCell(x, y, robotId, isReversing = false) {
    const key = `${x},${y}`;
    const now = Date.now();
    const existing = this.claimTable.get(key);

    // If currently occupied or reserved
    if (existing && existing.robotId !== robotId) {
      // Check if existing claim expired
      if (now > existing.expiresAt && existing.status !== 'REVERSING') {
        // Expired claim preempted
        this.claimTable.delete(key);
      } else {
        // Reversing robot gets absolute priority over entering robot
        if (isReversing && existing.status !== 'REVERSING') {
          this.claimTable.set(key, {
            robotId,
            claimTime: now,
            expiresAt: now + this.CLAIM_TIMEOUT_MS,
            status: 'REVERSING'
          });
          return { success: true, granted: true, priorityOverride: true };
        }
        return { 
          success: false, 
          holder: existing.robotId, 
          waitingSpot: this.cellLabels.get(key)?.waitingSpot || null 
        };
      }
    }

    // Grant reservation
    this.claimTable.set(key, {
      robotId,
      claimTime: now,
      expiresAt: now + this.CLAIM_TIMEOUT_MS,
      status: isReversing ? 'REVERSING' : 'RESERVED'
    });
    return { success: true, granted: true };
  }

  /**
   * Release reservation when robot returns to highway
   */
  releaseClaim(x, y, robotId) {
    const key = `${x},${y}`;
    const claim = this.claimTable.get(key);
    if (claim && claim.robotId === robotId) {
      this.claimTable.delete(key);
    }
  }

  /**
   * Claim entire Alley (Rear-entry mutual exclusion)
   */
  claimAlley(alleyId, robotId, isReversing = false) {
    const key = `alley_${alleyId}`;
    const now = Date.now();
    const existing = this.claimTable.get(key);

    if (existing && existing.robotId !== robotId) {
      if (now > existing.expiresAt && existing.status !== 'REVERSING') {
        this.claimTable.delete(key);
      } else {
        if (isReversing && existing.status !== 'REVERSING') {
          this.claimTable.set(key, { robotId, claimTime: now, expiresAt: now + this.CLAIM_TIMEOUT_MS, status: 'REVERSING' });
          return { success: true, granted: true };
        }
        return { success: false, holder: existing.robotId };
      }
    }

    this.claimTable.set(key, {
      robotId,
      claimTime: now,
      expiresAt: now + this.CLAIM_TIMEOUT_MS,
      status: isReversing ? 'REVERSING' : 'RESERVED'
    });
    return { success: true, granted: true };
  }

  releaseAlley(alleyId, robotId) {
    const key = `alley_${alleyId}`;
    const claim = this.claimTable.get(key);
    if (claim && claim.robotId === robotId) {
      this.claimTable.delete(key);
    }
  }

  /**
   * A* Pathfinding strictly obeying Highway + Buffer access rules.
   * AMRs cannot traverse buffer cells unless it is the explicit destination cell!
   */
  findHighwayPath(startX, startY, targetX, targetY, robotId, isTargetBuffer = false) {
    if (startX === targetX && startY === targetY) return [];

    const openSet = [];
    const cameFrom = new Map();
    const gScore = new Map();
    const fScore = new Map();

    const startKey = `${startX},${startY}`;
    gScore.set(startKey, 0);
    fScore.set(startKey, this.manhattan(startX, startY, targetX, targetY));
    openSet.push({ x: startX, y: startY, f: fScore.get(startKey) });

    const directions = [
      { dx: 1, dy: 0 },
      { dx: -1, dy: 0 },
      { dx: 0, dy: 1 },
      { dx: 0, dy: -1 }
    ];

    while (openSet.length > 0) {
      // Node with lowest fScore
      openSet.sort((a, b) => a.f - b.f);
      const current = openSet.shift();
      const curKey = `${current.x},${current.y}`;

      if (current.x === targetX && current.y === targetY) {
        return this.reconstructPath(cameFrom, current);
      }

      for (const dir of directions) {
        const nx = current.x + dir.dx;
        const ny = current.y + dir.dy;
        const neighborKey = `${nx},${ny}`;

        if (nx < 0 || nx >= this.width || ny < 0 || ny >= this.height) continue;

        const cellType = this.grid[nx][ny];

        // RACK or OBSTACLE is impassable
        if (cellType === CELL_TYPE.RACK || cellType === CELL_TYPE.OBSTACLE) continue;

        // BUFFER or TERMINAL_BUFFER can ONLY be entered if it is the target destination
        if (cellType === CELL_TYPE.BUFFER || cellType === CELL_TYPE.TERMINAL_BUFFER) {
          if (nx !== targetX || ny !== targetY) {
            continue; // Cannot cut through another rack's buffer or terminal buffer!
          }
        }

        // ALLEY check: can only enter if this robot has reserved the alley
        if (cellType === CELL_TYPE.ALLEY) {
          const info = this.cellLabels.get(neighborKey);
          if (info && info.alleyId) {
            const claim = this.claimTable.get(`alley_${info.alleyId}`);
            if (claim && claim.robotId !== robotId) {
              continue; // Alley is occupied by another peer
            }
          }
        }

        const tentativeG = (gScore.get(curKey) ?? Infinity) + 1;

        if (tentativeG < (gScore.get(neighborKey) ?? Infinity)) {
          cameFrom.set(neighborKey, { x: current.x, y: current.y });
          gScore.set(neighborKey, tentativeG);
          const f = tentativeG + this.manhattan(nx, ny, targetX, targetY);
          fScore.set(neighborKey, f);

          if (!openSet.some(item => item.x === nx && item.y === ny)) {
            openSet.push({ x: nx, y: ny, f });
          }
        }
      }
    }

    return null; // No path found
  }

  manhattan(x1, y1, x2, y2) {
    return Math.abs(x1 - x2) + Math.abs(y1 - y2);
  }

  reconstructPath(cameFrom, current) {
    const totalPath = [{ x: current.x, y: current.y }];
    let curKey = `${current.x},${current.y}`;
    while (cameFrom.has(curKey)) {
      const prev = cameFrom.get(curKey);
      totalPath.unshift({ x: prev.x, y: prev.y });
      curKey = `${prev.x},${prev.y}`;
    }
    return totalPath;
  }
}

// Export for browser & node environments
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { DecentralizedPlanner, CELL_TYPE };
}
