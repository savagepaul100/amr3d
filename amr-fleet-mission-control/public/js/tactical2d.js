/**
 * 2D TACTICAL WAREHOUSE MAP & INTERACTIVE CONTEXT MENU
 * High-definition 2D canvas with panning, zooming, path lines, V2V links, and right-click inspection.
 */

class Tactical2DView {
  constructor(canvasId, planner) {
    this.canvas = document.getElementById(canvasId);
    this.planner = planner;
    this.ctx = this.canvas ? this.canvas.getContext('2d') : null;

    this.camera = { x: 40, y: 25, scale: 16 };
    this.isDragging = false;
    this.dragStart = { x: 0, y: 0 };

    this.activeContextEntity = null; // Entity right-clicked

    this.initCanvasInteractions();
  }

  initCanvasInteractions() {
    if (!this.canvas) return;

    // Pan & Zoom
    this.canvas.addEventListener('mousedown', (e) => {
      if (e.button === 0) { // Left click pan
        this.isDragging = true;
        this.dragStart = { x: e.clientX, y: e.clientY };
      }
    });

    window.addEventListener('mousemove', (e) => {
      if (this.isDragging) {
        const dx = (e.clientX - this.dragStart.x) / this.camera.scale;
        const dy = (e.clientY - this.dragStart.y) / this.camera.scale;
        this.camera.x -= dx;
        this.camera.y -= dy;
        this.dragStart = { x: e.clientX, y: e.clientY };
      }
    });

    window.addEventListener('mouseup', () => {
      this.isDragging = false;
    });

    this.canvas.addEventListener('wheel', (e) => {
      e.preventDefault();
      const zoomFactor = e.deltaY < 0 ? 1.15 : 0.85;
      this.camera.scale = Math.max(6, Math.min(45, this.camera.scale * zoomFactor));
    });

    // Right-Click Context Menu
    this.canvas.addEventListener('contextmenu', (e) => {
      e.preventDefault();
      this.handleRightClick(e);
    });

    // Close Context Menu on click outside
    window.addEventListener('click', () => {
      const menu = document.getElementById('context-menu');
      if (menu) menu.classList.remove('show');
    });
  }

  handleRightClick(e) {
    const rect = this.canvas.getBoundingClientRect();
    const clickX = e.clientX - rect.left;
    const clickY = e.clientY - rect.top;

    // Convert pixel coords to grid coords
    const originX = this.canvas.width / 2 - this.camera.x * this.camera.scale;
    const originY = this.canvas.height / 2 - this.camera.y * this.camera.scale;

    const gridX = (clickX - originX) / this.camera.scale;
    const gridY = (clickY - originY) / this.camera.scale;

    const engine = window.app?.engine;
    if (!engine) return;

    // Check hit on AMRs
    let hitEntity = null;
    let hitType = null;

    for (const bot of engine.robots) {
      if (Math.hypot(bot.x - gridX, bot.y - gridY) < 1.2) {
        hitEntity = bot;
        hitType = 'amr';
        break;
      }
    }

    // Check hit on Humans
    if (!hitEntity) {
      for (const human of engine.humans) {
        if (Math.hypot(human.x - gridX, human.y - gridY) < 1.2) {
          hitEntity = human;
          hitType = 'human';
          break;
        }
      }
    }

    const menu = document.getElementById('context-menu');
    if (!menu) return;

    if (hitEntity) {
      this.activeContextEntity = { type: hitType, data: hitEntity };
      menu.style.left = `${e.clientX + 5}px`;
      menu.style.top = `${e.clientY + 5}px`;
      menu.classList.add('show');
      this.populateContextMenu(hitType, hitEntity);
    } else {
      menu.classList.remove('show');
    }
  }

  populateContextMenu(type, entity) {
    const menu = document.getElementById('context-menu');
    if (!menu) return;

    if (type === 'amr') {
      menu.innerHTML = `
        <div class="ctx-header">${entity.id} - AMR TELEMETRY</div>
        <div class="ctx-item" style="color:#94a3b8; font-size:11px;">
          Battery: <strong style="color:#10b981; margin-left:4px;">${entity.battery}%</strong> | Speed: ${entity.currentSpeed.toFixed(1)}m/s
        </div>
        <div class="ctx-item" style="color:#94a3b8; font-size:11px;">
          State: <strong style="color:#00e5ff; margin-left:4px;">${entity.state}</strong> (Floor ${entity.floor || 1})
        </div>
        <div class="ctx-item" onclick="window.app.manualController.setTarget('robot', '${entity.id}')">
          <span>Drive AMR (WASD)</span>
        </div>
        <div class="ctx-item" onclick="window.app.engine.spectateRobot('${entity.id}')">
          <span>Spectate in 3D Follow Cam</span>
        </div>
        <div class="ctx-item" onclick="window.app.engine.sendToFloor('${entity.id}', ${entity.floor === 1 ? 2 : 1})">
          <span>Take Elevator to Floor ${entity.floor === 1 ? 2 : 1}</span>
        </div>
        <div class="ctx-item" onclick="window.app.engine.sendToCharge(window.app.engine.robots.find(r => r.id === '${entity.id}'))">
          <span>Recall to Fast Charger</span>
        </div>
        <div class="ctx-item" style="color:#ef4444;" onclick="window.app.terminal.executeLine('halt ${entity.id}')">
          <span>Halt Robot</span>
        </div>
      `;
    } else if (type === 'human') {
      menu.innerHTML = `
        <div class="ctx-header">${entity.name} (HUMAN WORKER)</div>
        <div class="ctx-item" style="color:#94a3b8; font-size:11px;">
          Floor: ${entity.floor || 1} | Pos: (${entity.x.toFixed(1)}, ${entity.y.toFixed(1)})
        </div>
        <div class="ctx-item" onclick="window.app.manualController.setTarget('human', '${entity.id}')">
          <span>Control Worker (WASD)</span>
        </div>
        <div class="ctx-item" onclick="alert('Assigned patrol loop to ${entity.name}')">
          <span>Assign Patrol Corridor</span>
        </div>
      `;
    }
  }

  render(engine, room) {
    if (!this.ctx || !this.canvas || !engine) return;

    this.canvas.width = this.canvas.clientWidth;
    this.canvas.height = this.canvas.clientHeight;

    const ctx = this.ctx;
    const originX = this.canvas.width / 2 - this.camera.x * this.camera.scale;
    const originY = this.canvas.height / 2 - this.camera.y * this.camera.scale;
    const s = this.camera.scale;

    // Background
    ctx.fillStyle = '#080b11';
    ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

    ctx.save();
    ctx.translate(originX, originY);

    // Grid Floor
    ctx.strokeStyle = '#141a24';
    ctx.lineWidth = 0.5;
    for (let x = 0; x <= 80; x++) {
      ctx.beginPath();
      ctx.moveTo(x * s, 0);
      ctx.lineTo(x * s, 50 * s);
      ctx.stroke();
    }
    for (let y = 0; y <= 50; y++) {
      ctx.beginPath();
      ctx.moveTo(0, y * s);
      ctx.lineTo(80 * s, y * s);
      ctx.stroke();
    }

    // Draw Racks
    ctx.fillStyle = '#161b24';
    ctx.strokeStyle = '#272e3d';
    (room?.racks || []).forEach(r => {
      ctx.fillRect(r.x * s + 1, r.y * s + 1, s - 2, s - 2);
      ctx.strokeRect(r.x * s + 1, r.y * s + 1, s - 2, s - 2);
    });

    // Draw Charging Bays (Green)
    ctx.fillStyle = 'rgba(16, 185, 129, 0.2)';
    ctx.strokeStyle = '#10b981';
    (room?.chargers || []).forEach(ch => {
      ctx.fillRect(ch.x * s, ch.y * s, s, s);
      ctx.strokeRect(ch.x * s, ch.y * s, s, s);
      ctx.fillStyle = '#10b981';
      ctx.font = `${Math.max(8, s * 0.4)}px monospace`;
      ctx.fillText('⚡', ch.x * s + s * 0.2, ch.y * s + s * 0.7);
    });

    // Draw Inbound & Outbound Docks
    (room?.stations || []).forEach(st => {
      ctx.fillStyle = st.type === 'inbound' ? 'rgba(2, 132, 199, 0.3)' : 'rgba(217, 119, 6, 0.3)';
      ctx.strokeStyle = st.type === 'inbound' ? '#0284c7' : '#d97706';
      ctx.fillRect(st.x * s, st.y * s, s, s);
      ctx.strokeRect(st.x * s, st.y * s, s, s);
    });

    // Draw Elevator (Amber Hatching)
    (room?.elevators || []).forEach(elv => {
      ctx.fillStyle = 'rgba(245, 158, 11, 0.3)';
      ctx.strokeStyle = '#f59e0b';
      ctx.lineWidth = 1.5;
      ctx.fillRect(elv.x * s, elv.y * s, s * 1.5, s * 1.5);
      ctx.strokeRect(elv.x * s, elv.y * s, s * 1.5, s * 1.5);
      ctx.fillStyle = '#ffffff';
      ctx.font = `${Math.max(9, s * 0.4)}px sans-serif`;
      ctx.fillText('LIFT', elv.x * s + 2, elv.y * s + s);
    });

    // Draw Stairs (Yellow)
    (room?.stairs || []).forEach(st => {
      ctx.fillStyle = 'rgba(245, 158, 11, 0.25)';
      ctx.strokeStyle = '#f59e0b';
      ctx.fillRect(st.x * s, st.y * s, st.width * s, st.height * s);
      ctx.strokeRect(st.x * s, st.y * s, st.width * s, st.height * s);
      ctx.fillStyle = '#fff';
      ctx.font = `${Math.max(8, s * 0.35)}px sans-serif`;
      ctx.fillText('STAIRS', st.x * s + 4, st.y * s + s * 0.8);
    });

    // Draw C-V2X Mesh Laser Links
    ctx.strokeStyle = 'rgba(0, 229, 255, 0.35)';
    ctx.lineWidth = 1.2;
    for (let i = 0; i < engine.robots.length; i++) {
      for (let j = i + 1; j < engine.robots.length; j++) {
        const b1 = engine.robots[i];
        const b2 = engine.robots[j];
        if (Math.hypot(b1.x - b2.x, b1.y - b2.y) < 18) {
          ctx.beginPath();
          ctx.moveTo((b1.x + 0.5) * s, (b1.y + 0.5) * s);
          ctx.lineTo((b2.x + 0.5) * s, (b2.y + 0.5) * s);
          ctx.stroke();
        }
      }
    }

    // Draw AMRs
    engine.robots.forEach(bot => {
      const bx = (bot.x + 0.5) * s;
      const by = (bot.y + 0.5) * s;

      // Draw Path Breadcrumbs
      if (bot.path && bot.path.length > 0) {
        ctx.strokeStyle = bot.subState === 'REVERSING' ? 'rgba(245, 158, 11, 0.7)' : 'rgba(0, 229, 255, 0.6)';
        ctx.setLineDash([4, 2]);
        ctx.beginPath();
        ctx.moveTo(bx, by);
        bot.path.slice(bot.pathIndex).forEach(p => {
          ctx.lineTo((p.x + 0.5) * s, (p.y + 0.5) * s);
        });
        ctx.stroke();
        ctx.setLineDash([]);
      }

      // Safety Halo
      ctx.beginPath();
      ctx.arc(bx, by, s * 0.65, 0, Math.PI * 2);
      ctx.fillStyle = bot.state === 'HALTED' ? 'rgba(239, 68, 68, 0.3)' : 'rgba(16, 185, 129, 0.2)';
      ctx.fill();

      // AMR Body (Stark White & Dark Slate)
      ctx.save();
      ctx.translate(bx, by);
      ctx.rotate(bot.heading);

      ctx.fillStyle = '#141720';
      ctx.fillRect(-s * 0.38, -s * 0.28, s * 0.76, s * 0.56);
      ctx.fillStyle = '#ffffff';
      ctx.fillRect(-s * 0.32, -s * 0.22, s * 0.64, s * 0.44);

      // Heading Arrow
      ctx.fillStyle = '#00e5ff';
      ctx.beginPath();
      ctx.moveTo(s * 0.35, 0);
      ctx.lineTo(s * 0.15, -s * 0.12);
      ctx.lineTo(s * 0.15, s * 0.12);
      ctx.closePath();
      ctx.fill();

      ctx.restore();

      // Label
      ctx.fillStyle = '#ffffff';
      ctx.font = `${Math.max(9, s * 0.36)}px monospace`;
      ctx.fillText(bot.id, bx - s * 0.4, by - s * 0.45);
    });

    // Draw Humans
    engine.humans.forEach(h => {
      const hx = (h.x + 0.5) * s;
      const hy = (h.y + 0.5) * s;

      ctx.beginPath();
      ctx.arc(hx, hy, s * 0.32, 0, Math.PI * 2);
      ctx.fillStyle = h.gender === 'female' ? '#10b981' : '#f59e0b';
      ctx.fill();
      ctx.strokeStyle = '#ffffff';
      ctx.lineWidth = 1;
      ctx.stroke();

      ctx.fillStyle = '#cbd5e1';
      ctx.font = `${Math.max(8, s * 0.32)}px sans-serif`;
      ctx.fillText(h.name.split(' ')[0], hx - s * 0.3, hy - s * 0.4);
    });

    ctx.restore();
  }
}
