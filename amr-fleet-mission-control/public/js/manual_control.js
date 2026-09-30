/**
 * MANUAL CONTROL DRIVER FOR AMRS AND HUMAN WORKERS
 * Keyboard (WASD / Arrows) + On-Screen Control with Autonomous Collision Avoidance
 */

class ManualController {
  constructor(engine, planner) {
    this.engine = engine;
    this.planner = planner;
    this.targetEntity = null; // { type: 'robot'|'human', id: string, entityRef }
    this.isActive = false;

    this.keys = {
      forward: false,
      backward: false,
      left: false,
      right: false,
      brake: false
    };

    this.initKeyboardListeners();
  }

  setTarget(type, id) {
    if (!this.engine) return;
    let ref = null;
    if (type === 'robot') {
      ref = this.engine.robots.find(r => r.id === id);
    } else if (type === 'human') {
      ref = this.engine.humans.find(h => h.id === id);
    }

    if (ref) {
      this.targetEntity = { type, id, ref };
      this.isActive = true;
      ref.manualOverride = true;
      if (this.engine.showNotification) {
        this.engine.showNotification(`Manual Control Active: ${id} (WASD to Drive, ESC to Release)`);
      }
      this.updateHud();
    }
  }

  release() {
    if (this.targetEntity && this.targetEntity.ref) {
      this.targetEntity.ref.manualOverride = false;
    }
    this.targetEntity = null;
    this.isActive = false;
    this.updateHud();
  }

  initKeyboardListeners() {
    window.addEventListener('keydown', (e) => {
      if (!this.isActive) return;
      // Do not capture if user is typing in terminal or input box
      if (document.activeElement && (document.activeElement.tagName === 'INPUT' || document.activeElement.tagName === 'TEXTAREA')) {
        return;
      }

      switch (e.key.toLowerCase()) {
        case 'w':
        case 'arrowup':
          this.keys.forward = true;
          e.preventDefault();
          break;
        case 's':
        case 'arrowdown':
          this.keys.backward = true;
          e.preventDefault();
          break;
        case 'a':
        case 'arrowleft':
          this.keys.left = true;
          e.preventDefault();
          break;
        case 'd':
        case 'arrowright':
          this.keys.right = true;
          e.preventDefault();
          break;
        case ' ':
          this.keys.brake = true;
          e.preventDefault();
          break;
        case 'escape':
          this.release();
          e.preventDefault();
          break;
      }
      this.updateKeyVisuals();
    });

    window.addEventListener('keyup', (e) => {
      switch (e.key.toLowerCase()) {
        case 'w':
        case 'arrowup':
          this.keys.forward = false;
          break;
        case 's':
        case 'arrowdown':
          this.keys.backward = false;
          break;
        case 'a':
        case 'arrowleft':
          this.keys.left = false;
          break;
        case 'd':
        case 'arrowright':
          this.keys.right = false;
          break;
        case ' ':
          this.keys.brake = false;
          break;
      }
      this.updateKeyVisuals();
    });
  }

  /**
   * Called every physics/render tick
   */
  update(delta) {
    if (!this.isActive || !this.targetEntity || !this.targetEntity.ref) return;

    const ent = this.targetEntity.ref;
    const isRobot = this.targetEntity.type === 'robot';

    // Speed constants
    const maxSpeed = isRobot ? 2.5 : 1.4; // m/s
    const turnRate = isRobot ? 3.0 : 2.5; // rad/s
    const accel = 4.0;

    // Steering
    if (this.keys.left) {
      ent.heading = (ent.heading || 0) + turnRate * delta;
    }
    if (this.keys.right) {
      ent.heading = (ent.heading || 0) - turnRate * delta;
    }

    // Velocity update
    let targetV = 0;
    if (this.keys.forward && !this.keys.brake) targetV = maxSpeed;
    if (this.keys.backward && !this.keys.brake) targetV = -maxSpeed * 0.6; // Slower reverse

    // Smooth acceleration
    ent.currentSpeed = ent.currentSpeed || 0;
    if (ent.currentSpeed < targetV) {
      ent.currentSpeed = Math.min(targetV, ent.currentSpeed + accel * delta);
    } else if (ent.currentSpeed > targetV) {
      ent.currentSpeed = Math.max(targetV, ent.currentSpeed - accel * delta * 1.5);
    }

    // Dynamic Collision Check before moving
    if (Math.abs(ent.currentSpeed) > 0.01) {
      const stepDist = ent.currentSpeed * delta;
      const nextX = ent.x + Math.cos(ent.heading) * stepDist;
      const nextY = ent.y + Math.sin(ent.heading) * stepDist;

      // Obstacle detection
      const isBlocked = this.checkCollision(nextX, nextY, ent);
      if (!isBlocked) {
        ent.x = nextX;
        ent.y = nextY;
        if (isRobot) ent.ledStatus = 'GREEN';
      } else {
        ent.currentSpeed = 0; // Emergency Safety Stop
        if (isRobot) ent.ledStatus = 'RED'; // Red LED safety stop
      }
    }
  }

  checkCollision(x, y, selfEnt) {
    const gridX = Math.round(x);
    const gridY = Math.round(y);

    // Wall boundary
    if (gridX <= 0 || gridX >= (this.engine.gridWidth - 1) || gridY <= 0 || gridY >= (this.engine.gridHeight - 1)) {
      return true;
    }

    // Rack / Obstacle collision
    if (this.planner) {
      const cType = this.planner.grid[gridX]?.[gridY];
      if (cType === CELL_TYPE.RACK || cType === CELL_TYPE.OBSTACLE) {
        return true;
      }
    }

    // Proximity to other AMRs
    if (this.engine && this.engine.robots) {
      for (const bot of this.engine.robots) {
        if (bot === selfEnt) continue;
        const dist = Math.hypot(bot.x - x, bot.y - y);
        if (dist < 1.1) return true; // Safety distance
      }
    }

    // Proximity to Humans
    if (this.engine && this.engine.humans) {
      for (const human of this.engine.humans) {
        if (human === selfEnt) continue;
        const dist = Math.hypot(human.x - x, human.y - y);
        if (dist < 1.0) return true; // Safety distance
      }
    }

    return false;
  }

  updateHud() {
    const overlay = document.getElementById('manual-overlay');
    if (!overlay) return;
    if (this.isActive && this.targetEntity) {
      overlay.style.display = 'flex';
      const label = document.getElementById('manual-target-id');
      if (label) label.textContent = this.targetEntity.id;
    } else {
      overlay.style.display = 'none';
    }
  }

  updateKeyVisuals() {
    const setKey = (id, active) => {
      const el = document.getElementById(id);
      if (el) {
        if (active) el.classList.add('pressed');
        else el.classList.remove('pressed');
      }
    };
    setKey('key-w', this.keys.forward);
    setKey('key-a', this.keys.left);
    setKey('key-s', this.keys.backward);
    setKey('key-d', this.keys.right);
  }
}
