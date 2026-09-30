/**
 * AMR FLEET MISSION CONTROL - MASTER FRONTEND APP
 * Integrates 3D Engine, 2D Tactical View, Draggable Windows, '+' Dropdown, Captcha & Guide.
 */

class AMRApp {
  constructor() {
    this.planner = new DecentralizedPlanner(80, 50);
    this.roomManager = new RoomManager(this.planner);
    this.engine = new WarehouseEngine3D('viewport-3d', this.planner);
    this.tactical2D = new Tactical2DView('viewport-2d', this.planner);
    this.manualController = new ManualController(this.engine, this.planner);
    this.terminal = new TerminalBoss(this);
    this.captcha = null;

    this.selectedBotId = 'AMR-01';

    this.initUI();
    this.initMovableWindows();
    this.initDropdownMenu();
    this.initModalsAndGuide();
    this.startRenderLoops();
  }

  initUI() {
    // 3D vs 2D View Switch
    const btn3d = document.getElementById('tab-btn-3d');
    const btn2d = document.getElementById('tab-btn-2d');
    const view3d = document.getElementById('viewport-3d');
    const view2d = document.getElementById('viewport-2d');

    if (btn3d && btn2d) {
      btn3d.addEventListener('click', () => {
        btn3d.classList.add('active');
        btn2d.classList.remove('active');
        if (view3d) view3d.style.display = 'block';
        if (view2d) view2d.style.display = 'none';
      });

      btn2d.addEventListener('click', () => {
        btn2d.classList.add('active');
        btn3d.classList.remove('active');
        if (view3d) view3d.style.display = 'none';
        if (view2d) view2d.style.display = 'block';
      });
    }

    // Camera Preset Buttons
    document.querySelectorAll('.cam-preset-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.cam-preset-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        this.engine.setCameraMode(btn.getAttribute('data-mode'));
      });
    });

    // Visual Overlay Toggles
    const setupToggle = (btnId, toggleFn) => {
      const btn = document.getElementById(btnId);
      if (btn) {
        btn.addEventListener('click', () => {
          const state = toggleFn.call(this.engine);
          btn.classList.toggle('active', state);
        });
      }
    };
    setupToggle('btn-toggle-lidar', this.engine.toggleLidar);
    setupToggle('btn-toggle-paths', this.engine.togglePaths);
    setupToggle('btn-toggle-v2v', this.engine.toggleV2V);
    setupToggle('btn-toggle-workers', this.engine.toggleWorkers);

    // Halt All (Shows Confirmation Warning Window)
    const haltBtn = document.getElementById('btn-header-halt');
    if (haltBtn) {
      haltBtn.addEventListener('click', () => {
        this.showConfirmDialog(
          "WARNING: EMERGENCY SAFETY STOP",
          "Are you sure you want to halt all autonomous AMRs? Human workers will continue normal floor operations (ISO 3691-4).",
          () => {
            this.terminal.executeLine("halt all");
          }
        );
      });
    }

    // Quick Reset (Shows Confirmation Warning Window)
    const resetBtn = document.getElementById('btn-header-reset');
    if (resetBtn) {
      resetBtn.addEventListener('click', () => {
        this.showConfirmDialog(
          "CONFIRM WAREHOUSE QUICK RESET",
          "This will reset all inventory, AMRs, and tasks in test room 0123456789 back to original factory defaults.",
          () => {
            this.terminal.executeLine("reset");
          }
        );
      });
    }

    // Speed Cycle
    const speedBtn = document.getElementById('btn-header-speed');
    if (speedBtn) {
      const speeds = [1, 2, 5, 10];
      let sIdx = 0;
      speedBtn.addEventListener('click', () => {
        sIdx = (sIdx + 1) % speeds.length;
        const spd = speeds[sIdx];
        this.engine.setSimSpeed(spd);
        document.getElementById('speed-label-text').textContent = `${spd}x`;
      });
    }

    // Room Pill Click
    const roomPill = document.getElementById('room-pill');
    if (roomPill) {
      roomPill.addEventListener('click', () => {
        const modal = document.getElementById('room-modal');
        if (modal) modal.classList.remove('hidden');
      });
    }
  }

  /**
   * Generic Draggable Window Utility
   */
  initMovableWindows() {
    const makeDraggable = (win, handle) => {
      if (!win || !handle) return;
      let isDragging = false;
      let startX, startY, initLeft, initTop;

      handle.addEventListener('mousedown', (e) => {
        if (e.target.tagName === 'BUTTON' || e.target.tagName === 'INPUT') return;
        isDragging = true;
        startX = e.clientX;
        startY = e.clientY;
        const rect = win.getBoundingClientRect();
        initLeft = rect.left;
        initTop = rect.top;
        win.style.left = `${initLeft}px`;
        win.style.top = `${initTop}px`;
        win.style.right = 'auto';
        win.style.bottom = 'auto';
      });

      window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        win.style.left = `${initLeft + (e.clientX - startX)}px`;
        win.style.top = `${initTop + (e.clientY - startY)}px`;
      });

      window.addEventListener('mouseup', () => {
        isDragging = false;
      });
    };

    makeDraggable(document.getElementById('amr-inspector-window'), document.getElementById('inspector-drag-handle'));
    makeDraggable(document.getElementById('terminal-window'), document.getElementById('terminal-drag-handle'));
    makeDraggable(document.getElementById('guide-window'), document.getElementById('guide-drag-handle'));
  }

  initDropdownMenu() {
    const btn = document.getElementById('btn-add-dropdown');
    const menu = document.getElementById('add-dropdown-menu');

    if (btn && menu) {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        menu.classList.toggle('show');
      });

      window.addEventListener('click', () => {
        menu.classList.remove('show');
      });

      // Actions in dropdown
      const addActions = {
        'add-amr': () => {
          const num = this.engine.robots.length + 1;
          const id = `AMR-${String(num).padStart(2, '0')}`;
          const newBot = { id, x: 15, y: 24, floor: 1, heading: 0, battery: 100, state: 'IDLE', speed: 1.2, powerDraw: 320 };
          this.engine.robots.push(newBot);
          this.engine.createRobotMesh(newBot, num);
          this.terminal.logMove(id, "Commissioned into warehouse fleet.");
        },
        'add-rack': () => {
          alert("Click on any empty floor cell in 2D or 3D view to place storage rack pod.");
        },
        'add-charger': () => {
          alert("Fast charging bay installed at Maintenance Bay.");
        },
        'add-stair': () => {
          alert("Second Mezzanine industrial staircase added.");
        },
        'add-elevator': () => {
          this.terminal.printLog("Cargo Freight Elevator online. Use 'elev <id> <1|2>' to dispatch AMRs across floors.", "success");
        },
        'add-male-worker': () => {
          this.engine.spawnHuman(24, 20);
          this.terminal.printLog("Male human logistics technician deployed on floor.", "info");
        },
        'add-female-worker': () => {
          const id = `Worker-${this.engine.humans.length + 1}`;
          const newWorker = {
            id,
            name: `Ananya S.`,
            gender: 'female',
            vestColor: 0x10b981,
            pantsColor: 0x334155,
            x: 52,
            y: 20,
            floor: 1,
            heading: 0,
            path: [{x:52,y:20},{x:52,y:28},{x:58,y:28},{x:58,y:20}]
          };
          this.engine.humans.push(newWorker);
          this.engine.createHumanMesh(newWorker);
          this.terminal.printLog("Female human safety engineer deployed on floor.", "info");
        },
        'add-parcels': () => {
          this.engine.injectParcels(25);
          this.terminal.printLog("Injected 25 freight cartons into High-Bay Racks.", "success");
        }
      };

      document.querySelectorAll('.dropdown-item').forEach(item => {
        item.addEventListener('click', (e) => {
          e.stopPropagation();
          menu.classList.remove('show');
          const act = item.getAttribute('data-action');
          if (addActions[act]) addActions[act]();
        });
      });
    }
  }

  initModalsAndGuide() {
    // Captcha
    this.captcha = new NaturalHumanCaptcha('captcha-slot', (isHuman) => {
      const btn = document.getElementById('btn-room-connect');
      if (btn) btn.disabled = !isHuman;
    });

    const roomModal = document.getElementById('room-modal');
    const connectBtn = document.getElementById('btn-room-connect');
    if (connectBtn) {
      connectBtn.addEventListener('click', async () => {
        const input = document.getElementById('room-input');
        const code = input ? input.value.trim() : '0123456789';
        await this.loadRoom(code);
        if (roomModal) roomModal.classList.add('hidden');
      });
    }

    // Guide & About Modal (?)
    const helpBtn = document.getElementById('btn-header-help');
    const guideWin = document.getElementById('guide-window');
    if (helpBtn && guideWin) {
      helpBtn.addEventListener('click', () => {
        guideWin.style.display = guideWin.style.display === 'none' ? 'flex' : 'none';
      });
    }

    // Default room 0123456789 boot
    this.loadRoom('0123456789');
  }

  async loadRoom(roomId) {
    const data = await this.roomManager.loadRoom(roomId);
    this.engine.loadRoomData(data);
    const roomPillLabel = document.getElementById('room-id-display');
    if (roomPillLabel) roomPillLabel.textContent = roomId;
    this.terminal.printLog(`Connected to Warehouse Room: ${roomId}`, "success");
  }

  showConfirmDialog(title, message, onConfirm) {
    const overlay = document.getElementById('confirm-overlay');
    const titleEl = document.getElementById('confirm-title');
    const msgEl = document.getElementById('confirm-msg');
    const okBtn = document.getElementById('confirm-ok-btn');
    const cancelBtn = document.getElementById('confirm-cancel-btn');

    if (!overlay) {
      if (confirm(`${title}\n\n${message}`)) onConfirm();
      return;
    }

    titleEl.textContent = title;
    msgEl.textContent = message;
    overlay.classList.remove('hidden');

    const cleanup = () => {
      overlay.classList.add('hidden');
      okBtn.onclick = null;
      cancelBtn.onclick = null;
    };

    okBtn.onclick = () => { cleanup(); onConfirm(); };
    cancelBtn.onclick = () => { cleanup(); };
  }

  startRenderLoops() {
    // 2D Tactical Loop
    setInterval(() => {
      const view2d = document.getElementById('viewport-2d');
      if (view2d && view2d.style.display !== 'none') {
        this.tactical2D.render(this.engine, this.roomManager.activeRoom);
      }
    }, 1000 / 30);

    // Telemetry HUD Update
    setInterval(() => {
      this.updateInspectorHUD();
    }, 200);
  }

  updateInspectorHUD() {
    const bot = this.engine.robots.find(r => r.id === this.selectedBotId) || this.engine.robots[0];
    if (!bot) return;

    const setTxt = (id, val) => {
      const el = document.getElementById(id);
      if (el) el.textContent = val;
    };

    setTxt('insp-bot-id', bot.id);
    setTxt('insp-bot-soc', `${bot.battery}%`);
    setTxt('insp-bot-speed', `${(bot.currentSpeed || 0).toFixed(2)} m/s`);
    setTxt('insp-bot-state', bot.subState === 'REVERSING' ? 'REVERSING' : bot.state);
    setTxt('insp-bot-floor', `Floor ${bot.floor || 1}`);
    setTxt('insp-bot-pos', `(${bot.x.toFixed(1)}, ${bot.y.toFixed(1)})`);
    setTxt('insp-bot-power', `${bot.powerDraw || 380} W (DMS Edge: 28W)`);
    setTxt('insp-bot-task', bot.task || 'Autonomous Transit');
  }
}

window.addEventListener('DOMContentLoaded', () => {
  window.app = new AMRApp();
});
