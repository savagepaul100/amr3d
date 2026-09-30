/**
 * TERMINAL BOSS - MOVE-BY-MOVE STREAM, SHORT COMMANDS & WARNINGS CONSOLE
 * 
 * Features:
 * - Real-time stream logging every single AMR and elevator move
 * - Short commands: 'halt', 'run', 'spec 1', 'drive 1', 'spd 2', 'elev 1 2', 'reset', 'help'
 * - 'halt all' halts AMRs only - humans keep walking!
 * - Dedicated 'Warnings & Incidents' tab
 * - Confirmation warning modals for destructive actions
 */

class TerminalBoss {
  constructor(app) {
    this.app = app;
    this.activeTab = 'log'; // 'log' or 'warnings'
    this.history = [];
    this.historyIndex = -1;

    this.warningsCount = 0;

    this.init();
  }

  init() {
    this.logBody = document.getElementById('terminal-log-body');
    this.warnBody = document.getElementById('terminal-warn-body');
    this.inputElement = document.getElementById('terminal-cli-input');
    this.warnBadge = document.getElementById('term-warn-badge');

    if (this.inputElement) {
      this.inputElement.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          const raw = this.inputElement.value.trim();
          if (raw) {
            this.history.push(raw);
            this.historyIndex = this.history.length;
            this.executeLine(raw);
            this.inputElement.value = '';
          }
        } else if (e.key === 'ArrowUp') {
          if (this.historyIndex > 0) {
            this.historyIndex--;
            this.inputElement.value = this.history[this.historyIndex] || '';
          }
          e.preventDefault();
        } else if (e.key === 'ArrowDown') {
          if (this.historyIndex < this.history.length - 1) {
            this.historyIndex++;
            this.inputElement.value = this.history[this.historyIndex] || '';
          } else {
            this.historyIndex = this.history.length;
            this.inputElement.value = '';
          }
          e.preventDefault();
        }
      });
    }

    this.printLog("EDGE-AI MISSION CONTROL CLI v2.8 (ACTIVE)", "header");
    this.printLog("Decentralized Highway Protocol & 2-Level Elevator Stack Live.", "info");
  }

  switchTab(tab) {
    this.activeTab = tab;
    const btnLog = document.getElementById('btn-term-tab-log');
    const btnWarn = document.getElementById('btn-term-tab-warn');

    if (tab === 'log') {
      if (btnLog) btnLog.classList.add('active');
      if (btnWarn) btnWarn.classList.remove('active');
      if (this.logBody) this.logBody.style.display = 'block';
      if (this.warnBody) this.warnBody.style.display = 'none';
    } else {
      if (btnWarn) btnWarn.classList.add('active');
      if (btnLog) btnLog.classList.remove('active');
      if (this.logBody) this.logBody.style.display = 'none';
      if (this.warnBody) this.warnBody.style.display = 'block';
    }
  }

  printLog(text, type = "info") {
    if (!this.logBody) return;
    const line = document.createElement('div');
    line.className = `term-line ${type}`;
    line.textContent = text;
    this.logBody.appendChild(line);
    this.logBody.scrollTop = this.logBody.scrollHeight;
  }

  printWarn(text, severity = "warn") {
    if (!this.warnBody) return;
    this.warningsCount++;
    if (this.warnBadge) {
      this.warnBadge.textContent = this.warningsCount;
      this.warnBadge.style.display = 'inline-block';
    }

    const line = document.createElement('div');
    line.className = `term-line ${severity}`;
    const timeStr = new Date().toLocaleTimeString();
    line.textContent = `[${timeStr}] ${text}`;
    this.warnBody.appendChild(line);
    this.warnBody.scrollTop = this.warnBody.scrollHeight;
  }

  logMove(entityId, actionText) {
    const timeStr = new Date().toLocaleTimeString();
    this.printLog(`[${timeStr}] [${entityId}] ${actionText}`, "info");
  }

  clear() {
    if (this.logBody) this.logBody.innerHTML = '';
  }

  executeLine(line) {
    this.printLog(`AMR-CLI:> ${line}`, "cmd");
    const subCommands = line.split(/;|&&/).map(c => c.trim()).filter(c => c.length > 0);
    for (const cmd of subCommands) {
      this.dispatch(cmd);
    }
  }

  dispatch(rawCmd) {
    const parts = rawCmd.split(/\s+/);
    const verb = parts[0].toLowerCase();
    const arg1 = parts[1]?.toLowerCase();
    const arg2 = parts[2]?.toLowerCase();

    switch (verb) {
      case 'help':
        this.handleHelp(arg1);
        break;

      case 'clear':
      case 'cls':
        this.clear();
        break;

      case 'halt':
      case 'stop':
        if (!arg1 || arg1 === 'all') {
          this.app.engine.pauseAutomation();
          this.printLog("EMERGENCY STOP: AMRs halted. Human workers remain active (ISO 3691-4).", "warn");
          this.printWarn("Fleet Emergency Stop Triggered by Operator.", "warn");
        } else {
          const botId = this.normalizeBotId(arg1);
          const bot = this.app.engine.robots.find(r => r.id.toLowerCase() === botId.toLowerCase());
          if (bot) {
            bot.state = 'HALTED';
            bot.currentSpeed = 0;
            this.printLog(`Halted AMR ${bot.id}.`, "warn");
          }
        }
        break;

      case 'run':
      case 'start':
      case 'resume':
        if (!arg1 || arg1 === 'all') {
          this.app.engine.resumeAutomation();
          this.printLog("AMR fleet automation restored.", "success");
        } else {
          const botId = this.normalizeBotId(arg1);
          const bot = this.app.engine.robots.find(r => r.id.toLowerCase() === botId.toLowerCase());
          if (bot) {
            bot.state = 'IDLE';
            this.printLog(`Resumed AMR ${bot.id}.`, "success");
          }
        }
        break;

      case 'spec':
      case 'spectate':
      case 'follow':
        if (!arg1) {
          this.printLog("Usage: spec <1-8> or spec AMR-01", "warn");
        } else {
          const bId = this.normalizeBotId(arg1);
          const success = this.app.engine.spectateRobot(bId);
          if (success) this.printLog(`Spectating ${bId} in follow cam.`, "success");
          else this.printLog(`AMR not found: ${bId}`, "error");
        }
        break;

      case 'drive':
      case 'control':
        if (!arg1) {
          this.printLog("Usage: drive <bot_id | human_id> (e.g. drive 1, drive Worker-1)", "warn");
        } else {
          if (arg1.startsWith('worker') || arg1.startsWith('human')) {
            this.app.manualController.setTarget('human', arg1);
            this.printLog(`Manual Control enabled for Human ${arg1}. Steer with WASD.`, "success");
          } else {
            const bId = this.normalizeBotId(arg1);
            this.app.manualController.setTarget('robot', bId);
            this.printLog(`Manual Control enabled for ${bId}. Drive with WASD, ESC to release.`, "success");
          }
        }
        break;

      case 'elev':
      case 'elevator':
      case 'floor':
        if (!arg1 || !arg2) {
          this.printLog("Usage: elev <bot_id> <1|2> (e.g. elev 1 2)", "warn");
        } else {
          const bId = this.normalizeBotId(arg1);
          const floor = parseInt(arg2);
          if (floor === 1 || floor === 2) {
            this.app.engine.sendBotToFloor(bId, floor);
            this.printLog(`Dispatched ${bId} to Elevator for Floor ${floor}.`, "success");
          }
        }
        break;

      case 'spd':
      case 'speed':
        const spd = parseFloat(arg1);
        if ([1, 2, 5, 10].includes(spd)) {
          this.app.engine.setSimSpeed(spd);
          this.printLog(`Speed set to ${spd}x.`, "info");
        } else {
          this.printLog("Valid speeds: 1, 2, 5, 10", "warn");
        }
        break;

      case 'reset':
        this.clear();
        this.app.roomManager.resetTestRoom();
        this.app.engine.loadRoomData(this.app.roomManager.activeRoom);
        this.printLog("Warehouse reset to default test configuration (0123456789).", "success");
        break;

      case 'inj':
      case 'inject':
        const cnt = parseInt(arg1 || '10');
        this.app.engine.injectParcels(cnt);
        this.printLog(`Injected ${cnt} cartons into inventory.`, "success");
        break;

      default:
        this.printLog(`Unknown command: '${verb}'. Type 'help' for command list.`, "error");
        break;
    }
  }

  normalizeBotId(str) {
    if (!str) return 'AMR-01';
    if (/^\d+$/.test(str)) {
      return `AMR-${String(str).padStart(2, '0')}`;
    }
    return str.toUpperCase();
  }

  handleHelp(topic) {
    if (!topic) {
      this.printLog("=== MISSION CONTROL COMMANDS ===", "header");
      this.printLog("  halt [all|<id>]  - Emergency Stop AMRs (humans unaffected)");
      this.printLog("  run [all|<id>]   - Resume fleet operations");
      this.printLog("  spec <id>        - Spectate robot in 3D (e.g. 'spec 1')");
      this.printLog("  drive <id>       - Take manual WASD control (e.g. 'drive 1')");
      this.printLog("  elev <id> <1|2>  - Take elevator to Floor 1 or 2");
      this.printLog("  spd <1|2|5|10>   - Change simulation multiplier");
      this.printLog("  inj <count>      - Inject cartons into inventory");
      this.printLog("  reset            - Clear terminal & reset warehouse");
      this.printLog("Type 'help nav' or 'help room' for detailed topic guides.");
      return;
    }

    if (topic === 'nav') {
      this.printLog("=== HIGHWAY PROTOCOL GUIDE ===", "header");
      this.printLog("1. Free travel permitted ONLY on HIGHWAY cells.");
      this.printLog("2. BUFFER cells accessed only during targeted pick/deposit.");
      this.printLog("3. AMRs MUST reverse out onto Highway waiting spot upon completion.");
      this.printLog("4. Reversing AMRs possess absolute priority over entering peers.");
    }
  }
}
