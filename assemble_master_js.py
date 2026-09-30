# assemble_master_js.py

master_code = '''/**
 * EDGE-AI AMR MISSION CONTROL - MASTER INTEGRATION SUITE (SIH 26123 - Bharat Electronics Limited)
 * 
 * Full Capabilities:
 * - Professional SVG Icons Throughout (Zero Emojis)
 * - Modern Compact Header with Dropdown Menus (Zoom & Resolution Resilient)
 * - Removal of ISO & Orbit buttons from header row; clean Cam dropdown
 * - Bottom Bar Legend completely moved to the '?' Help & About Modal
 * - Real 3D & 2D Raycast Spawning at Exact Right-Click Coordinates
 * - Full Dynamic Entity Creation (AMRs with 3D models & paths, Male & Female Human Workers, Pallet Carts)
 * - Two Dedicated Terminals:
 *     Terminal 1: Real-Time Telemetry & Update Stream
 *     Terminal 2: Interactive Command Console (CLI Boss) with Vast Command Set & State Modification
 * - Settings Menu (Speed Presets, Bulk Ingest, Reset, Emergency Halt)
 * - First-Time Visit 10-Digit Warehouse ID Modal with Natural Curvature Captcha & Random ID Generator
 * - LiDAR & Next-Destination Path Toggles
 * - 2-Level Mezzanine Deck, 2 Steel Staircases & Animated Freight Elevator
 * - Diverse Human Workforce (Male & Female) with Real Grid Collision AI
 * - Manual WASD Tele-Operation Demonstrating LiDAR Safety Detection
 * - Draggable Windows Throughout
 */

(function() {
  'use strict';

  // =========================================================================
  // 1. PROFESSIONAL SVG ICONS (ZERO EMOJIS)
  // =========================================================================
  const SVG = {
    robot: `<svg viewBox="0 0 24 24" width="14" height="14" stroke="currentColor" stroke-width="2" fill="none"><rect x="3" y="11" width="18" height="10" rx="2"></rect><circle cx="12" cy="5" r="2"></circle><path d="M12 7v4"></path><line x1="8" y1="16" x2="8" y2="16"></line><line x1="16" y1="16" x2="16" y2="16"></line></svg>`,
    map: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"></polygon><line x1="8" y1="2" x2="8" y2="18"></line><line x1="16" y1="6" x2="16" y2="22"></line></svg>`,
    terminal: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><polyline points="4 17 10 11 4 5"></polyline><line x1="12" y1="19" x2="20" y2="19"></line></svg>`,
    alert: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>`,
    cam: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"></path><circle cx="12" cy="13" r="4"></circle></svg>`,
    layers: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>`,
    plus: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2.5" fill="none"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>`,
    gear: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>`,
    help: `<svg viewBox="0 0 24 24" width="14" height="14" stroke="currentColor" stroke-width="2" fill="none"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>`,
    cube: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>`,
    grid: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>`,
    crosshair: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><circle cx="12" cy="12" r="10"></circle><line x1="22" y1="12" x2="18" y2="12"></line><line x1="6" y1="12" x2="2" y2="12"></line><line x1="12" y1="6" x2="12" y2="2"></line><line x1="12" y1="22" x2="12" y2="18"></line></svg>`,
    top: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><line x1="12" y1="5" x2="12" y2="19"></line><polyline points="19 12 12 19 5 12"></polyline></svg>`,
    lidar: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><path d="M12 22a10 10 0 0 0 10-10"></path><path d="M12 18a6 6 0 0 0 6-6"></path><path d="M12 14a2 2 0 0 0 2-2"></path><circle cx="12" cy="12" r="1" fill="currentColor"></circle></svg>`,
    path: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><circle cx="4" cy="19" r="2"></circle><circle cx="20" cy="5" r="2"></circle><path d="M6 19c6-2 6-12 12-14"></path></svg>`,
    wire: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><rect x="3" y="3" width="18" height="18" rx="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="3" y1="15" x2="21" y2="15"></line><line x1="9" y1="3" x2="9" y2="21"></line><line x1="15" y1="3" x2="15" y2="21"></line></svg>`,
    v2v: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><line x1="12" y1="20" x2="12" y2="10"></line><circle cx="12" cy="10" r="2"></circle><path d="M4.93 4.93a10 10 0 0 1 14.14 0"></path><path d="M7.76 7.76a6 6 0 0 1 8.48 0"></path></svg>`,
    worker: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>`,
    pallet: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg>`,
    elevator: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><rect x="4" y="2" width="16" height="20" rx="2"></rect><polyline points="8 10 12 6 16 10"></polyline><polyline points="8 14 12 18 16 14"></polyline></svg>`,
    reset: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><polyline points="1 4 1 10 7 10"></polyline><path d="M3.51 15a9 9 0 1 0 2.13-9.36L1 10"></path></svg>`,
    halt: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><rect x="6" y="4" width="4" height="16"></rect><rect x="14" y="4" width="4" height="16"></rect></svg>`,
    check: `<svg viewBox="0 0 24 24" width="14" height="14" stroke="currentColor" stroke-width="3" fill="none"><polyline points="20 6 9 17 4 12"></polyline></svg>`,
    book: `<svg viewBox="0 0 24 24" width="14" height="14" stroke="currentColor" stroke-width="2" fill="none"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>`,
    tools: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"></path></svg>`,
    rack: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><rect x="3" y="3" width="18" height="18" rx="1"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="3" y1="15" x2="21" y2="15"></line><line x1="9" y1="3" x2="9" y2="21"></line><line x1="15" y1="3" x2="15" y2="21"></line></svg>`,
    parcel: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>`,
    cone: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><path d="M12 2L4 20h16L12 2z"></path><line x1="8" y1="14" x2="16" y2="14"></line></svg>`,
    cart: `<svg viewBox="0 0 24 24" width="13" height="13" stroke="currentColor" stroke-width="2" fill="none"><rect x="2" y="7" width="20" height="10" rx="1"></rect><circle cx="6" cy="19" r="2"></circle><circle cx="18" cy="19" r="2"></circle></svg>`
  };

  window.SVG_ICONS = SVG;

  // =========================================================================
  // 2. MODERN COMPACT STYLING INJECTION (RESPONSIVE & ZOOM-PROOF)
  // =========================================================================
  function injectModernStyles() {
    const styleId = 'modern-mission-control-css';
    if (document.getElementById(styleId)) return;

    const css = `
      /* Header & Branding */
      .modern-header {
        background: #0d1117 !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.12) !important;
        padding: 0 14px !important;
        height: 50px !important;
        max-height: 50px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        gap: 10px !important;
        flex-shrink: 0 !important;
        z-index: 100 !important;
        box-sizing: border-box !important;
        overflow: visible !important;
      }
      .brand-section {
        display: flex;
        align-items: center;
        gap: 10px;
        flex-shrink: 0;
      }
      .robot-brand-logo {
        display: flex;
        align-items: center;
        gap: 7px;
        cursor: pointer;
        padding: 3px 6px;
        border-radius: 6px;
        transition: background 0.15s;
      }
      .robot-brand-logo:hover {
        background: rgba(255, 255, 255, 0.06);
      }
      .brand-text {
        display: flex;
        flex-direction: column;
        line-height: 1;
      }
      .brand-name {
        font-weight: 900;
        font-size: 15px;
        letter-spacing: 0.8px;
        color: #fff;
      }
      .brand-sub {
        font-size: 8px;
        color: #38bdf8;
        font-weight: 700;
        letter-spacing: 0.5px;
      }
      .room-pill {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: #151a24;
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 12px;
        padding: 3px 8px;
        font-size: 10px;
        color: #cbd5e1;
        cursor: pointer;
        transition: all 0.15s ease;
      }
      .room-pill:hover {
        border-color: #38bdf8;
        background: #1c2230;
      }
      .status-pulse-dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: #10b981;
        box-shadow: 0 0 6px #10b981;
      }
      .room-pill-id {
        font-family: ui-monospace, monospace;
        font-weight: 700;
        color: #fff;
      }

      /* Center Tabs */
      .header-nav-tabs {
        display: flex;
        align-items: center;
        gap: 4px;
        flex-shrink: 0;
      }
      .h-nav-tab {
        background: #131722;
        border: 1px solid rgba(255, 255, 255, 0.1);
        color: #94a3b8;
        font-size: 11.5px;
        font-weight: 600;
        padding: 5px 12px;
        border-radius: 6px;
        display: flex;
        align-items: center;
        gap: 6px;
        cursor: pointer;
        transition: all 0.15s ease;
      }
      .h-nav-tab:hover {
        background: #1c2230;
        color: #fff;
        border-color: rgba(255, 255, 255, 0.25);
      }
      .h-nav-tab.active {
        background: #232938;
        color: #fff;
        border-color: #fff;
      }

      /* Right Actions & Dropdowns */
      .header-action-group {
        display: flex;
        align-items: center;
        gap: 6px;
        flex-shrink: 0;
      }
      .icon-toggle-group {
        display: flex;
        background: #090c12;
        padding: 2px;
        border-radius: 6px;
        border: 1px solid rgba(255, 255, 255, 0.12);
      }
      .icon-toggle-btn {
        background: transparent;
        border: none;
        color: #94a3b8;
        padding: 4px 7px;
        border-radius: 4px;
        cursor: pointer;
        display: flex;
        align-items: center;
        font-size: 11px;
        transition: all 0.15s;
      }
      .icon-toggle-btn.active {
        background: #1e2433;
        color: #fff;
        box-shadow: 0 1px 4px rgba(0,0,0,0.5);
      }
      .dropdown-trigger-btn {
        background: #131722;
        border: 1px solid rgba(255, 255, 255, 0.12);
        color: #cbd5e1;
        border-radius: 6px;
        padding: 5px 9px;
        font-size: 11px;
        font-weight: 600;
        display: inline-flex;
        align-items: center;
        gap: 5px;
        cursor: pointer;
        transition: all 0.15s ease;
      }
      .dropdown-trigger-btn:hover {
        background: #1c2230;
        color: #fff;
        border-color: rgba(255, 255, 255, 0.3);
      }
      .dropdown-trigger-btn.highlight {
        border-color: #38bdf8;
        color: #38bdf8;
        background: rgba(56, 189, 248, 0.1);
      }
      .icon-btn {
        background: #131722;
        border: 1px solid rgba(255, 255, 255, 0.12);
        color: #cbd5e1;
        width: 32px;
        height: 32px;
        border-radius: 6px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        transition: all 0.15s ease;
      }
      .icon-btn:hover {
        background: #1c2230;
        color: #fff;
        border-color: #fff;
      }
      .icon-btn.highlight-btn {
        border-color: rgba(255, 255, 255, 0.3);
        color: #fff;
      }

      /* Dropdown Menus */
      .mc-dropdown {
        position: relative;
        display: inline-block;
      }
      .mc-dropdown-menu {
        position: absolute;
        top: calc(100% + 5px);
        right: 0;
        background: #11141c;
        border: 1px solid rgba(255, 255, 255, 0.18);
        border-radius: 8px;
        padding: 5px;
        min-width: 200px;
        box-shadow: 0 16px 36px rgba(0, 0, 0, 0.85);
        z-index: 1000;
        display: none;
      }
      .mc-dropdown-menu.show {
        display: block;
      }
      .mc-dropdown-item {
        padding: 7px 10px;
        font-size: 11.5px;
        color: #cbd5e1;
        border-radius: 5px;
        display: flex;
        align-items: center;
        gap: 8px;
        cursor: pointer;
        transition: all 0.12s;
      }
      .mc-dropdown-item:hover {
        background: #1e2433;
        color: #fff;
      }
      .mc-dropdown-item.active {
        color: #38bdf8;
        font-weight: 700;
      }
      .mc-dropdown-item.danger {
        color: #fca5a5;
      }
      .mc-dropdown-item.danger:hover {
        background: rgba(239, 68, 68, 0.2);
        color: #fff;
      }
      .dropdown-divider {
        height: 1px;
        background: rgba(255, 255, 255, 0.08);
        margin: 4px 0;
      }
      .dropdown-menu-title {
        font-size: 9px;
        font-weight: 700;
        color: #64748b;
        padding: 4px 8px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
      }
      .speed-pill {
        flex: 1;
        background: #181d28;
        border: 1px solid rgba(255,255,255,0.1);
        color: #94a3b8;
        border-radius: 4px;
        padding: 3px 0;
        font-size: 10px;
        cursor: pointer;
        text-align: center;
      }
      .speed-pill:hover, .speed-pill.active {
        background: #273042;
        color: #fff;
        border-color: #38bdf8;
      }

      /* Dual Terminal Workspace */
      .th-panes.mode-split {
        display: flex !important;
        flex-direction: row !important;
        gap: 0 !important;
        height: 100% !important;
      }
      .th-pane {
        overflow: hidden !important;
      }
      .terminal-cli-console-screen {
        scrollbar-width: thin;
        scrollbar-color: rgba(255,255,255,0.2) transparent;
      }
      .terminal-cli-input-bar {
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 8px 12px;
        background: #11141c;
        border-top: 1px solid rgba(255, 255, 255, 0.12);
      }
      .cli-prompt-symbol {
        font-family: monospace;
        font-weight: 700;
        color: #38bdf8;
        font-size: 12px;
      }
      .cli-input-field {
        flex: 1;
        background: #090c12;
        border: 1px solid rgba(255, 255, 255, 0.15);
        color: #fff;
        padding: 5px 10px;
        font-size: 11.5px;
        font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
        border-radius: 5px;
        outline: none;
      }
      .cli-input-field:focus {
        border-color: #38bdf8;
        box-shadow: 0 0 6px rgba(56, 189, 248, 0.3);
      }

      /* Legend Grid inside ? Modal */
      .legend-grid-modal {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 8px;
        margin-top: 6px;
      }
      .legend-card-item {
        display: flex;
        align-items: center;
        gap: 10px;
        background: #0b0e14;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 6px;
        padding: 6px 10px;
        font-size: 11px;
      }
      .legend-swatch {
        width: 14px;
        height: 14px;
        border-radius: 3px;
        flex-shrink: 0;
      }

      
      .mc-prompt-btn {
        background: #0284c7;
        color: #fff;
        border: none;
        border-radius: 6px;
        padding: 4px 10px;
        font-size: 11px;
        font-weight: 700;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 4px;
        box-shadow: 0 0 10px rgba(2, 132, 199, 0.5);
        animation: pulse-border 1.5s infinite;
      }
      .mc-prompt-btn.charge {
        background: #16a34a;
        box-shadow: 0 0 10px rgba(22, 163, 74, 0.5);
      }
      .mc-prompt-btn.drop {
        background: #ea580c;
        box-shadow: 0 0 10px rgba(234, 88, 12, 0.5);
      }
      @keyframes pulse-border {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
      }

      /* Manual Tele-Op HUD Banner */
      #manual-ctrl-overlay {
        position: absolute;
        bottom: 24px;
        left: 50%;
        transform: translateX(-50%);
        background: rgba(14, 18, 25, 0.94);
        border: 1px solid #fff;
        border-radius: 8px;
        padding: 8px 18px;
        display: none;
        align-items: center;
        gap: 16px;
        z-index: 500;
        box-shadow: 0 8px 30px rgba(0,0,0,0.8);
        backdrop-filter: blur(8px);
      }
      .manual-key-badge {
        display: inline-block;
        background: #222938;
        border: 1px solid rgba(255,255,255,0.3);
        border-radius: 4px;
        padding: 2px 7px;
        font-family: monospace;
        font-size: 11px;
        font-weight: 700;
        color: #fff;
      }

      /* Context Menu */
      #mc-context-menu {
        position: fixed;
        background: #121620;
        border: 1px solid rgba(255, 255, 255, 0.25);
        border-radius: 8px;
        padding: 6px;
        min-width: 230px;
        box-shadow: 0 12px 32px rgba(0,0,0,0.85);
        z-index: 10000;
        display: none;
      }
      .ctx-header {
        padding: 6px 10px;
        border-bottom: 1px solid rgba(255,255,255,0.1);
        margin-bottom: 4px;
      }
      .ctx-title {
        font-weight: 700;
        font-size: 12px;
        color: #fff;
      }
      .ctx-sub {
        font-size: 10px;
        color: #94a3b8;
      }
      .ctx-item {
        padding: 7px 10px;
        font-size: 11.5px;
        color: #cbd5e1;
        border-radius: 4px;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 8px;
        transition: all 0.12s;
      }
      .ctx-item:hover {
        background: #1f2638;
        color: #fff;
      }
      .ctx-item.danger:hover {
        background: rgba(239, 68, 68, 0.25);
        color: #f87171;
      }

      /* Generic Modal Dialog */
      .mc-modal-backdrop {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background: rgba(0, 0, 0, 0.75);
        backdrop-filter: blur(5px);
        display: none;
        align-items: center;
        justify-content: center;
        z-index: 10001;
      }
      .mc-modal-card {
        background: #11141c;
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 10px;
        width: 480px;
        max-width: 90vw;
        box-shadow: 0 20px 50px rgba(0,0,0,0.9);
        overflow: hidden;
      }
      .mc-modal-header {
        padding: 12px 18px;
        background: #161b24;
        border-bottom: 1px solid rgba(255,255,255,0.12);
        display: flex;
        align-items: center;
        justify-content: space-between;
      }
      .mc-modal-body {
        padding: 18px;
        font-size: 12.5px;
        line-height: 1.5;
        color: #cbd5e1;
      }
      .mc-modal-footer {
        padding: 12px 18px;
        background: #141822;
        border-top: 1px solid rgba(255,255,255,0.12);
        display: flex;
        justify-content: flex-end;
        gap: 10px;
      }

      /* Modern Clean Captcha & Solid Modal Backdrop */
      #modal-room-switch {
        background: #06080d !important;
        backdrop-filter: none !important;
        -webkit-backdrop-filter: none !important;
      }
      .natural-captcha-widget {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: #0d121c;
        border: 1px solid rgba(255, 255, 255, 0.16);
        border-radius: 8px;
        padding: 14px 18px;
        margin: 16px 0;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.45);
        cursor: pointer;
        user-select: none;
        transition: border-color 0.2s, background 0.2s;
      }
      .natural-captcha-widget:hover {
        border-color: rgba(56, 189, 248, 0.4);
        background: #101624;
      }
      .captcha-checkbox {
        width: 26px;
        height: 26px;
        border: 2px solid #64748b;
        border-radius: 6px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        background: #151b27;
        transition: all 0.18s ease;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.4);
        flex-shrink: 0;
      }
      .captcha-checkbox:hover {
        border-color: #38bdf8;
        box-shadow: 0 0 8px rgba(56, 189, 248, 0.35);
      }
      .captcha-checkbox.verified {
        border-color: #10b981;
        background: #10b981;
        box-shadow: 0 0 12px rgba(16, 185, 129, 0.45);
      }
      .captcha-checkbox.verified svg {
        display: block !important;
      }
    `;

    const el = document.createElement('style');
    el.id = styleId;
    el.textContent = css;
    document.head.appendChild(el);
  }

  // =========================================================================
  // 3. DROPDOWN CONTROLLER
  // =========================================================================
  window.toggleDropdown = function(id) {
    const target = document.getElementById(id);
    const all = document.querySelectorAll('.mc-dropdown-menu');
    all.forEach(m => {
      if (m !== target) m.classList.remove('show');
    });
    if (target) target.classList.toggle('show');
  };

  window.closeAllDropdowns = function() {
    const all = document.querySelectorAll('.mc-dropdown-menu');
    all.forEach(m => m.classList.remove('show'));
  };

  window.addEventListener('click', (e) => {
    if (!e.target.closest('.mc-dropdown')) {
      closeAllDropdowns();
    }
  });

  window.setSimMultiplier = function(speed) {
    window.simSpeed = speed;
    const btns = document.querySelectorAll('.speed-pill');
    btns.forEach(b => {
      b.classList.toggle('active', b.textContent.includes(String(speed)));
    });
    if (typeof logTerminal === 'function') {
      logTerminal('SYSTEM', 'tag-overtake', `Simulation warp speed set to ${speed}x.`);
    }
  };

  // =========================================================================
  // 4. RAYCAST GRID COORDINATE DETECTOR & EXACT SPAWNING
  // =========================================================================
  let lastRightClickGrid = { x: 40, y: 25 };

  function getExactClickedGrid(e) {
    let gx = 40, gy = 25;
    const is3D = window.viewMode === '3D' || (document.getElementById('viewport-3d') && document.getElementById('viewport-3d').style.display !== 'none');

    // 1. Exact Mathematical Raycast in 3D Viewport
    if (is3D && window.camera3D && typeof THREE !== 'undefined') {
      const container = document.getElementById('viewport-3d');
      if (container) {
        const rect = container.getBoundingClientRect();
        const mouse = new THREE.Vector2(
          ((e.clientX - rect.left) / rect.width) * 2 - 1,
          -((e.clientY - rect.top) / rect.height) * 2 + 1
        );
        const raycaster = window.raycaster3D || new THREE.Raycaster();
        raycaster.setFromCamera(mouse, window.camera3D);
        const floorPlane = new THREE.Plane(new THREE.Vector3(0, 1, 0), 0);
        const pt = new THREE.Vector3();
        const hit = raycaster.ray.intersectPlane(floorPlane, pt);
        if (hit) {
          const cSize = window.C_SIZE || 1.6;
          const halfW = window.HALF_W || 40;
          const halfH = window.HALF_H || 25;
          gx = Math.round(pt.x / cSize + halfW - 0.5);
          gy = Math.round(pt.z / cSize + halfH - 0.5);
        }
      }
    } 
    // 2. 2D Canvas Coordinate Conversion
    else if (typeof window.screenToGrid === 'function') {
      const canvas = document.getElementById('viewport');
      if (canvas) {
        const rect = canvas.getBoundingClientRect();
        const pt = window.screenToGrid(e.clientX - rect.left, e.clientY - rect.top);
        if (pt) {
          gx = pt.x;
          gy = pt.y;
        }
      }
    }

    gx = Math.max(1, Math.min(78, gx));
    gy = Math.max(1, Math.min(48, gy));
    return { x: gx, y: gy };
  }

  // =========================================================================
  // 5. TRUE 3D + 2D COLLISION-AVOIDING EXACT SPAWNERS
  // =========================================================================
  function isSpawnPointFree(gx, gy) {
    if (!window.mapData) return true;
    const w = window.mapData.width || 80;
    const h = window.mapData.height || 50;
    if (gx <= 1 || gx >= w - 2 || gy <= 1 || gy >= h - 2) return false;
    
    // Check rack grid (cannot spawn inside a physical rack)
    if (window.mapData.grid && window.mapData.grid[gx] && window.mapData.grid[gx][gy] === 1) {
      return false;
    }

    // Check collision with existing AMRs (clearance radius 1.25m)
    if (window.AMR_FLEET) {
      for (const bot of window.AMR_FLEET) {
        if (Math.hypot(bot.x - gx, bot.y - gy) < 1.25) return false;
      }
    }

    // Check collision with existing human workers or static obstacles
    if (window.DYNAMIC_OBSTACLES) {
      for (const obs of window.DYNAMIC_OBSTACLES) {
        if (Math.hypot(obs.x - gx, obs.y - gy) < 1.25) return false;
      }
    }

    return true;
  }

  function findSafeSpawnPoint(targetX, targetY) {
    const startX = Math.round(targetX);
    const startY = Math.round(targetY);

    if (isSpawnPointFree(startX, startY)) {
      return { x: startX, y: startY };
    }

    // Spiral search outward for nearest legal free clearance cell
    for (let r = 1; r <= 8; r++) {
      for (let dx = -r; dx <= r; dx++) {
        for (let dy = -r; dy <= r; dy++) {
          if (Math.abs(dx) !== r && Math.abs(dy) !== r) continue;
          const candidateX = startX + dx;
          const candidateY = startY + dy;
          if (isSpawnPointFree(candidateX, candidateY)) {
            return { x: candidateX, y: candidateY };
          }
        }
      }
    }

    return { x: Math.max(2, Math.min(77, startX)), y: Math.max(2, Math.min(47, startY)) };
  }

  window.registerAndSpawnAmr = function(customX = null, customY = null) {
    if (!window.AMR_FLEET) return;
    const targetX = customX !== null ? customX : lastRightClickGrid.x;
    const targetY = customY !== null ? customY : lastRightClickGrid.y;
    const safe = findSafeSpawnPoint(targetX, targetY);
    const x = safe.x;
    const y = safe.y;

    const idx = window.AMR_FLEET.length + 1;
    const newId = idx < 10 ? `AMR-0${idx}` : `AMR-${idx}`;

    const newBot = {
      id: newId,
      num: idx,
      homeBayId: `CH-0${(idx % 8) + 1}`,
      assignedBayId: `CH-0${(idx % 8) + 1}`,
      currentChargerId: null,
      targetChargerId: null,
      homeBayZone: 'NORTH',
      homeX: x,
      homeY: y,
      x: x,
      y: y,
      gridX: Math.round(x),
      gridY: Math.round(y),
      heading: 0,
      state: 'IDLE',
      battery: 100.0,
      cargo: null,
      carriedParcels: [],
      isLoadedYellow: false,
      orderBox: null,
      payloadWeight: 0,
      manualOverride: false,
      path: [],
      pathIndex: 0,
      speed: 1.0,
      currentSpeed: 0,
      isWaiting: false,
      isRerouting: false,
      isOvertaking: false,
      floor: 1
    };
    window.AMR_FLEET.push(newBot);

    // Create authentic 3D robot model & add to scene3D at exact coordinate
    if (window.scene3D && typeof window.createRealAMR3D === 'function') {
      const amrObj = window.createRealAMR3D(newId, idx);
      if (window.gridTo3D) {
        const wp = window.gridTo3D(x, y, 0);
        amrObj.root.position.set(wp.x, 0, wp.z);
      }
      if (window.amrModels3D) window.amrModels3D[newId] = amrObj;
      window.scene3D.add(amrObj.root);

      // Create 3D trajectory line ribbon
      if (typeof THREE !== 'undefined') {
        const lineGeo = new THREE.BufferGeometry();
        const positions = new Float32Array(120 * 3);
        lineGeo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        const lineMat = new THREE.LineDashedMaterial({
          color: 0xffffff,
          dashSize: 0.8,
          gapSize: 0.4,
          transparent: true,
          opacity: 0.55
        });
        const line = new THREE.Line(lineGeo, lineMat);
        line.computeLineDistances();
        line.visible = window.show3DPaths !== false;
        window.scene3D.add(line);
        if (window.pathLineObjects3D) window.pathLineObjects3D[newId] = line;
      }
    }

    if (typeof window.render === 'function') window.render();
    const msg = `[SPAWN] AMR ${newId} placed safely at (${x}, ${y}) avoiding all object collisions.`;
    if (typeof logTerminal === 'function') logTerminal('SYSTEM', 'tag-overtake', msg);
    if (window.terminalBoss) window.terminalBoss.printCli(msg, 'success');
  };

  window.registerAndSpawnHuman = function(customX = null, customY = null, gender = 'male') {
    if (!window.DYNAMIC_OBSTACLES) return;
    const targetX = customX !== null ? customX : lastRightClickGrid.x;
    const targetY = customY !== null ? customY : lastRightClickGrid.y;
    const safe = findSafeSpawnPoint(targetX, targetY);
    const x = safe.x;
    const y = safe.y;

    const idx = window.DYNAMIC_OBSTACLES.length + 1;
    const id = `HUMAN-${String(idx).padStart(2, '0')}`;
    const name = gender === 'female' ? `Operator Elena ${idx}` : `Operator Rajesh ${idx}`;
    const color = gender === 'female' ? 0xf97316 : 0x10b981;
    const cssColor = gender === 'female' ? '#f97316' : '#10b981';

    const newWorker = {
      id: id,
      type: 'human',
      name: name,
      gender: gender,
      role: gender === 'female' ? 'Safety Auditor' : 'Inventory Specialist',
      color: color,
      cssColor: cssColor,
      x: x,
      y: y,
      gridX: Math.round(x),
      gridY: Math.round(y),
      floor: 1,
      speed: 0.85,
      heading: 0,
      routeIndex: 0,
      pauseTimer: 0,
      isPaused: false,
      safetyRadius: 1.5,
      currentAction: 'Patrolling Corridor',
      route: [
        { x: x, y: y },
        { x: Math.min(78, x + 6), y: y },
        { x: Math.min(78, x + 6), y: Math.min(48, y + 8) },
        { x: x, y: Math.min(48, y + 8) }
      ]
    };
    window.DYNAMIC_OBSTACLES.push(newWorker);

    // Create 3D procedural human model & position at exact safe coordinate
    if (window.scene3D && typeof window.createHuman3DModel === 'function') {
      const hModel = window.createHuman3DModel(newWorker);
      if (window.gridTo3D) {
        const wp = window.gridTo3D(x, y, 0);
        hModel.root.position.set(wp.x, 0, wp.z);
      }
      if (window.humanModels3D) window.humanModels3D[id] = hModel;
      window.scene3D.add(hModel.root);
    }

    if (typeof window.render === 'function') window.render();
    const msg = `[SPAWN] Human Operator ${name} (${gender.toUpperCase()}) entered warehouse at safe clearance (${x}, ${y}).`;
    if (typeof logTerminal === 'function') logTerminal('SYSTEM', 'tag-overtake', msg);
    if (window.terminalBoss) window.terminalBoss.printCli(msg, 'success');
  };

  window.registerAndSpawnRack = function(customX = null, customY = null) {
    if (!window.mapData || !window.mapData.grid) return;
    const targetX = customX !== null ? customX : lastRightClickGrid.x;
    const targetY = customY !== null ? customY : lastRightClickGrid.y;
    const x = Math.max(2, Math.min(window.mapData.width - 3, Math.round(targetX)));
    const y = Math.max(2, Math.min(window.mapData.height - 3, Math.round(targetY)));

    window.mapData.grid[x][y] = 1;

    const cat = typeof window.getRackCategory === 'function' ? window.getRackCategory(y) : {
      sku: 'SKU-GEN',
      name: 'General Storage',
      fullName: 'General Warehouse Storage Rack',
      color: '#38bdf8',
      tint: '#0284c7',
      border: '#0369a1'
    };

    if (typeof window.rackMemory !== 'undefined') {
      const rackKey = `${x},${y}`;
      window.rackMemory[rackKey] = {
        x: x,
        y: y,
        id: `RACK-${x}-${y}`,
        categorySku: cat.sku || 'SKU-GEN',
        categoryName: cat.name || 'General Storage',
        categoryFullName: cat.fullName || 'General Warehouse Storage Rack',
        categoryColor: cat.color || '#38bdf8',
        categoryTint: cat.tint || '#0284c7',
        categoryBorder: cat.border || '#0369a1',
        floors: [null, null, null, null, null],
        capacity: 5
      };

      // Seed 2-3 yellow parcel boxes onto the new rack
      const parcelCount = Math.floor(Math.random() * 2) + 2;
      for (let f = 0; f < parcelCount; f++) {
        const pSeq = Math.floor(1000 + Math.random() * 9000);
        window.rackMemory[rackKey].floors[f] = {
          parcel_id: `PKG-${pSeq}`,
          sku: cat.sku || 'SKU-GEN',
          name: cat.name || 'General Storage',
          weight: `${(10 + Math.random() * 8).toFixed(1)}kg`
        };
      }
    }

    if (window.scene3D && typeof THREE !== 'undefined' && typeof window.gridTo3D === 'function') {
      const rackGroup = new THREE.Group();
      rackGroup.name = `spawnedRack_${x}_${y}`;
      const cSize = window.C_SIZE || 1.6;
      const halfCell = cSize * 0.44;

      // 4 upright steel corner posts
      const postGeo = new THREE.BoxGeometry(0.06, 2.4, 0.06);
      const postMat = new THREE.MeshStandardMaterial({ color: 0x181c26, roughness: 0.5, metalness: 0.5 });
      const corners = [
        [-halfCell, -halfCell],
        [halfCell, -halfCell],
        [-halfCell, halfCell],
        [halfCell, halfCell]
      ];
      for (const [cx, cz] of corners) {
        const post = new THREE.Mesh(postGeo, postMat);
        post.position.set(cx, 1.2, cz);
        rackGroup.add(post);
      }

      // 5 horizontal shelf decks
      const shelfGeo = new THREE.BoxGeometry(cSize * 0.92, 0.035, cSize * 0.92);
      const shelfMat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.2, metalness: 0.2 });
      const tierHeights = [0.45, 0.90, 1.35, 1.80, 2.25];
      for (const th of tierHeights) {
        const shelf = new THREE.Mesh(shelfGeo, shelfMat);
        shelf.position.set(0, th, 0);
        rackGroup.add(shelf);
      }

      const pos = window.gridTo3D(x, y, 0);
      rackGroup.position.set(pos.x, 0, pos.z);
      window.scene3D.add(rackGroup);

      if (typeof window.update3DRacksTotes === 'function') {
        window.update3DRacksTotes();
      }
    }

    if (typeof window.render === 'function') window.render();
    const msg = `[SPAWN] Storage Rack installed at grid (${x}, ${y}) with 5 tiers.`;
    if (typeof logTerminal === 'function') logTerminal('SYSTEM', 'tag-overtake', msg);
    if (window.terminalBoss) window.terminalBoss.printCli(msg, 'success');
  };

  window.registerAndSpawnParcel = function(customX = null, customY = null) {
    if (!window.DYNAMIC_OBSTACLES) return;
    const targetX = customX !== null ? customX : lastRightClickGrid.x;
    const targetY = customY !== null ? customY : lastRightClickGrid.y;
    const safe = findSafeSpawnPoint(targetX, targetY);
    const x = safe.x;
    const y = safe.y;

    const idx = window.DYNAMIC_OBSTACLES.length + 1;
    const parcelId = 'PKG-' + Math.floor(1000 + Math.random() * 9000);
    const weight = (2.5 + Math.random() * 8.5).toFixed(1);
    const newBox = {
      id: `BOX-${String(idx).padStart(2, '0')}`,
      type: 'parcel_box',
      name: `Freight Parcel ${parcelId}`,
      parcel_id: parcelId,
      weight: parseFloat(weight),
      role: 'Staging Parcel',
      x: x,
      y: y,
      gridX: Math.round(x),
      gridY: Math.round(y),
      isStatic: true,
      safetyRadius: 0.85,
      currentAction: 'Floor Freight Parcel'
    };
    window.DYNAMIC_OBSTACLES.push(newBox);

    if (window.scene3D && typeof window.createParcelBox3DModel === 'function') {
      const cModel = window.createParcelBox3DModel(newBox);
      if (window.gridTo3D && cModel && cModel.root) {
        const wp = window.gridTo3D(x, y, 0);
        cModel.root.position.set(wp.x, 0, wp.z);
      }
      if (window.obstacleModels3D) window.obstacleModels3D[newBox.id] = cModel;
      if (cModel && cModel.root) window.scene3D.add(cModel.root);
    }

    if (typeof window.render === 'function') window.render();
    const msg = `[SPAWN] Freight Parcel ${parcelId} (${weight}kg) staged at (${x}, ${y}). Ready for AMR pickup.`;
    if (typeof logTerminal === 'function') logTerminal('INBOUND', 'tag-inbound', msg);
    if (window.terminalBoss) window.terminalBoss.printCli(msg, 'success');
  };

  window.registerAndSpawnHurdle = function(customX = null, customY = null) {
    if (!window.DYNAMIC_OBSTACLES) return;
    const targetX = customX !== null ? customX : lastRightClickGrid.x;
    const targetY = customY !== null ? customY : lastRightClickGrid.y;
    const safe = findSafeSpawnPoint(targetX, targetY);
    const x = safe.x;
    const y = safe.y;

    const idx = window.DYNAMIC_OBSTACLES.length + 1;
    const id = `HURDLE-${String(idx).padStart(2, '0')}`;
    const newHurdle = {
      id: id,
      type: 'hurdle',
      name: `Hazard Hurdle #${idx}`,
      role: 'Safety Zone Hazard',
      x: x,
      y: y,
      gridX: Math.round(x),
      gridY: Math.round(y),
      isStatic: true,
      safetyRadius: 1.25,
      currentAction: 'Aisle Caution Perimeter'
    };
    window.DYNAMIC_OBSTACLES.push(newHurdle);

    if (window.scene3D && typeof window.createHurdle3DModel === 'function') {
      const hObj = window.createHurdle3DModel(newHurdle);
      if (window.gridTo3D && hObj && hObj.root) {
        const wp = window.gridTo3D(x, y, 0);
        hObj.root.position.set(wp.x, 0, wp.z);
      }
      if (window.obstacleModels3D) window.obstacleModels3D[id] = hObj;
      if (hObj && hObj.root) window.scene3D.add(hObj.root);
    }

    if (typeof window.render === 'function') window.render();
    const msg = `[WARN] Safety Hazard Hurdle ${id} placed at (${x}, ${y}). Fleet A* dynamic detours active.`;
    if (typeof logTerminal === 'function') logTerminal('SAFETY', 'tag-yield', msg);
    if (window.terminalBoss) window.terminalBoss.printCli(msg, 'warn');
  };

  window.registerAndSpawnPalletCart = function(customX = null, customY = null) {
    if (!window.DYNAMIC_OBSTACLES) return;
    const targetX = customX !== null ? customX : lastRightClickGrid.x;
    const targetY = customY !== null ? customY : lastRightClickGrid.y;
    const safe = findSafeSpawnPoint(targetX, targetY);
    const x = safe.x;
    const y = safe.y;

    const idx = window.DYNAMIC_OBSTACLES.length + 1;
    const id = `CART-${String(idx).padStart(2, '0')}`;
    const newCart = {
      id: id,
      type: 'pallet_cart',
      name: `Pallet Cart #${idx}`,
      role: 'Staging Pallet',
      x: x,
      y: y,
      gridX: Math.round(x),
      gridY: Math.round(y),
      isStatic: true,
      safetyRadius: 1.25,
      currentAction: 'Staging Pallet'
    };
    window.DYNAMIC_OBSTACLES.push(newCart);

    if (window.scene3D && typeof window.createPalletCart3DModel === 'function') {
      const cModel = window.createPalletCart3DModel(newCart);
      if (window.gridTo3D && cModel && cModel.root) {
        const wp = window.gridTo3D(x, y, 0);
        cModel.root.position.set(wp.x, 0, wp.z);
      }
      if (window.obstacleModels3D) window.obstacleModels3D[id] = cModel;
      if (cModel && cModel.root) window.scene3D.add(cModel.root);
    }

    if (typeof window.render === 'function') window.render();
    const msg = `[SPAWN] Staging pallet cart placed at safe clearance (${x}, ${y}).`;
    if (typeof logTerminal === 'function') logTerminal('SYSTEM', 'tag-yield', msg);
    if (window.terminalBoss) window.terminalBoss.printCli(msg, 'info');
  };

  // =========================================================================
  // 6. ACCURATE RIGHT-CLICK CONTEXT MENU
  // =========================================================================
  function initAccurateContextMenu() {
    const menu = document.getElementById('mc-context-menu');
    const titleEl = document.getElementById('ctx-menu-title');
    const subEl = document.getElementById('ctx-menu-sub');
    const itemsEl = document.getElementById('ctx-menu-items');

    window.addEventListener('click', () => {
      if (menu) menu.style.display = 'none';
    });

    const handler = (e) => {
      const target = e.target;
      if (!target.closest('#viewport') && !target.closest('#viewport-3d')) return;

      e.preventDefault();

      const coords = getExactClickedGrid(e);
      lastRightClickGrid = coords;

      let clickedBot = null;
      let clickedHuman = null;

      if (window.AMR_FLEET) {
        for (const b of window.AMR_FLEET) {
          if (Math.hypot(b.x - coords.x, b.y - coords.y) < 1.4) {
            clickedBot = b;
            break;
          }
        }
      }

      if (!clickedBot && window.DYNAMIC_OBSTACLES) {
        for (const h of window.DYNAMIC_OBSTACLES) {
          if (Math.hypot(h.x - coords.x, h.y - coords.y) < 1.4) {
            clickedHuman = h;
            break;
          }
        }
      }

      itemsEl.innerHTML = '';

      if (clickedBot) {
        const b = clickedBot;
        titleEl.textContent = `AMR ${b.id}`;
        subEl.textContent = `Battery: ${Math.round(b.battery)}% | Pos: (${Math.round(b.x)}, ${Math.round(b.y)}) | State: ${b.state}`;

        itemsEl.innerHTML = `
          <div class="ctx-item" onclick="setManualControl('robot', '${b.id}')">
            ${SVG.crosshair} Take Control
          </div>

          <div class="ctx-item" onclick="terminalBoss.execute('spec ${b.id}')">
            ${SVG.cam} Follow in 3D Camera
          </div>
          <div class="ctx-item danger" onclick="terminalBoss.execute('halt ${b.id}')">
            ${SVG.halt} Emergency Halt AMR
          </div>
        `;
      } else if (clickedHuman) {
        const h = clickedHuman;
        titleEl.textContent = `${h.name} (${h.gender ? h.gender.toUpperCase() : 'STAFF'})`;
        subEl.textContent = `${h.role || 'Warehouse Operator'} | Pos: (${Math.round(h.x)}, ${Math.round(h.y)})`;

        itemsEl.innerHTML = `
          <div class="ctx-item" onclick="setManualControl('human', '${h.id}')">
            ${SVG.worker} Take Control
          </div>
          <div class="ctx-item" onclick="terminalBoss.printCli('Employee ${h.name} (${h.id}) | Role: ${h.role} | Heart Rate: 72 bpm | Shift: Active', 'info')">
            ${SVG.terminal} View Personnel Telemetry
          </div>
        `;
      } else {
        titleEl.innerHTML = `<span style="display:flex; align-items:center; gap:6px;">${SVG.grid} COORDINATES: <strong>X: ${coords.x}, Y: ${coords.y}</strong></span>`;
        subEl.textContent = `Spawn at (${coords.x}, ${coords.y}) or CLI: 'add amr ${coords.x} ${coords.y}'`;

        itemsEl.innerHTML = `
          <div class="ctx-item" onclick="registerAndSpawnAmr(${coords.x}, ${coords.y})">
            ${SVG.robot} Spawn Autonomous AMR (X: ${coords.x}, Y: ${coords.y})
          </div>
          <div class="ctx-item" onclick="registerAndSpawnHuman(${coords.x}, ${coords.y}, 'male')">
            ${SVG.worker} Spawn Male Worker (X: ${coords.x}, Y: ${coords.y})
          </div>
          <div class="ctx-item" onclick="registerAndSpawnHuman(${coords.x}, ${coords.y}, 'female')">
            ${SVG.worker} Spawn Female Worker (X: ${coords.x}, Y: ${coords.y})
          </div>
          <div class="ctx-item" onclick="registerAndSpawnRack(${coords.x}, ${coords.y})">
            ${SVG.rack} Spawn Storage Rack (X: ${coords.x}, Y: ${coords.y})
          </div>
          <div class="ctx-item" onclick="registerAndSpawnParcel(${coords.x}, ${coords.y})">
            ${SVG.parcel} Spawn Freight Parcel (X: ${coords.x}, Y: ${coords.y})
          </div>
          <div class="ctx-item" onclick="registerAndSpawnHurdle(${coords.x}, ${coords.y})">
            ${SVG.cone} Spawn Hazard Hurdle / Cone (X: ${coords.x}, Y: ${coords.y})
          </div>
          <div class="ctx-item" onclick="registerAndSpawnPalletCart(${coords.x}, ${coords.y})">
            ${SVG.pallet} Spawn Pallet Cart (X: ${coords.x}, Y: ${coords.y})
          </div>
        `;
      }

      menu.style.left = `${Math.min(window.innerWidth - 240, e.clientX)}px`;
      menu.style.top = `${Math.min(window.innerHeight - 260, e.clientY)}px`;
      menu.style.display = 'block';
    };

    window.addEventListener('contextmenu', handler);
  }

  // =========================================================================
  // 7. TERMINAL 2: INTERACTIVE COMMAND CONSOLE (CLI BOSS)
  // =========================================================================
  class CommandTerminalBoss {
    constructor() {
      this.history = [];
      this.historyIdx = -1;
      this.consoleEl = null;
    }

    init() {
      this.consoleEl = document.getElementById('terminal-cli-console');
      const input = document.getElementById('terminal-cli-input');
      if (!input) return;

      input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
          const val = input.value.trim();
          if (val) {
            this.history.push(val);
            this.historyIdx = this.history.length;
            this.execute(val);
            input.value = '';
          }
        } else if (e.key === 'ArrowUp') {
          if (this.historyIdx > 0) {
            this.historyIdx--;
            input.value = this.history[this.historyIdx] || '';
          }
          e.preventDefault();
        } else if (e.key === 'ArrowDown') {
          if (this.historyIdx < this.history.length - 1) {
            this.historyIdx++;
            input.value = this.history[this.historyIdx] || '';
          } else {
            this.historyIdx = this.history.length;
            input.value = '';
          }
          e.preventDefault();
        }
      });
    }

    printCli(text, type = 'info') {
      if (!this.consoleEl) this.consoleEl = document.getElementById('terminal-cli-console');
      if (!this.consoleEl) return;

      const line = document.createElement('div');
      const colors = {
        cmd: '#38bdf8',
        success: '#4ade80',
        warn: '#fbbf24',
        error: '#f87171',
        info: '#cbd5e1'
      };
      line.style.color = colors[type] || '#cbd5e1';
      line.style.marginBottom = '2px';
      line.innerHTML = text;

      this.consoleEl.appendChild(line);
      this.consoleEl.scrollTop = this.consoleEl.scrollHeight;
    }

    clearConsole() {
      if (this.consoleEl) {
        this.consoleEl.innerHTML = '<div style="color:#64748b; font-size:10px;">[CONSOLE CLEARED] Type commands below.</div>';
      }
    }

    execute(raw) {
      this.printCli(`AMR-CLI:&gt; ${raw}`, 'cmd');
      const stmts = raw.split(/;|&&/).map(s => s.trim()).filter(s => s.length > 0);
      for (const cmd of stmts) {
        this.dispatchCommand(cmd);
      }
    }

    dispatchCommand(cmd) {
      const parts = cmd.split(/\\s+/);
      const verb = parts[0].toLowerCase();
      const arg1 = parts[1]?.toLowerCase();
      const arg2 = parts[2]?.toLowerCase();
      const arg3 = parts[3]?.toLowerCase();

      switch (verb) {
        case 'help':
          this.showHelpManual(arg1);
          break;

        case 'clear':
        case 'cls':
          this.clearConsole();
          break;

        case 'status':
          this.showFleetStatus(arg1);
          break;

        case 'halt':
        case 'stop':
          if (!arg1 || arg1 === 'all') {
            window.fleetHalted = true;
            if (window.AMR_FLEET) {
              window.AMR_FLEET.forEach(r => {
                r.currentSpeed = 0;
                if (r.state !== 'HALTED' && r.state !== 'IDLE_CHARGING') {
                  r.previousState = r.state;
                  r.state = 'HALTED';
                }
              });
            }
            this.printCli("EMERGENCY FLEET HALT: All AMRs stopped. Human workers remain active (ISO 3691-4).", "warn");
            if (typeof logTerminal === 'function') logTerminal('SYSTEM', 'tag-traffic', "[HALT] Emergency Stop All AMRs.");
          } else {
            const bot = this.resolveBot(arg1);
            if (bot) {
              bot.state = 'HALTED';
              bot.currentSpeed = 0;
              this.printCli(`Halted robot ${bot.id}.`, "warn");
            } else {
              this.printCli(`Robot not found: ${arg1}`, "error");
            }
          }
          break;

        case 'run':
        case 'start':
        case 'resume':
          window.fleetHalted = false;
          if (arg1 && arg1 !== 'all') {
            const bot = this.resolveBot(arg1);
            if (bot) {
              bot.state = 'IDLE';
              this.printCli(`Resumed robot ${bot.id}.`, "success");
            } else {
              this.printCli(`Robot not found: ${arg1}`, "error");
            }
          } else {
            if (window.AMR_FLEET) {
              window.AMR_FLEET.forEach(b => {
                if (b.state === 'HALTED') {
                  b.state = b.previousState || 'IDLE';
                }
              });
            }
            this.printCli("Fleet automation active. All AMRs cruising.", "success");
            if (typeof logTerminal === 'function') logTerminal('SYSTEM', 'tag-overtake', "[RUN] Fleet automation resumed.");
          }
          break;

        case 'spec':
        case 'follow':
          if (!arg1) {
            this.printCli("Usage: spec <bot_id> (e.g. 'spec 1' or 'spec AMR-03')", "warn");
          } else {
            const bot = this.resolveBot(arg1);
            if (bot) {
              window.trackedRobotId = bot.id;
              window.trackCameraFollow = true;
              if (typeof setCameraMode === 'function') setCameraMode('follow');
              this.printCli(`Camera locked on ${bot.id}.`, "success");
            }
          }
          break;

        case 'drive':
        case 'control':
          if (!arg1) {
            this.printCli("Usage: drive <bot_id | worker_name> (e.g. 'drive 1')", "warn");
          } else {
            if (arg1.startsWith('human') || arg1.startsWith('work') || arg1.startsWith('jane') || arg1.startsWith('raj')) {
              setManualControl('human', arg1);
              this.printCli(`Manual tele-operation engaged for human operator. WASD to walk, ESC to release.`, "success");
            } else {
              const bot = this.resolveBot(arg1);
              if (bot) {
                setManualControl('robot', bot.id);
                this.printCli(`Manual tele-operation engaged for ${bot.id}. WASD to drive, ESC to release.`, "success");
              }
            }
          }
          break;

        case 'elev':
        case 'floor':
          if (!arg1 || !arg2) {
            this.printCli("Usage: elev <bot_id> <1|2> (e.g. 'elev 1 2')", "warn");
          } else {
            const bot = this.resolveBot(arg1);
            const floor = parseInt(arg2, 10);
            if (bot && (floor === 1 || floor === 2)) {
              dispatchAmrToFloor(bot.id, floor);
              this.printCli(`AMR ${bot.id} ordered to Freight Elevator for Floor ${floor}.`, "success");
            }
          }
          break;

        case 'speed':
        case 'spd':
          const spd = parseFloat(arg1);
          if ([0.5, 1, 2, 5].includes(spd)) {
            setSimMultiplier(spd);
            this.printCli(`Simulation speed set to ${spd}x.`, "success");
          } else {
            this.printCli("Valid speeds: 0.5, 1, 2, 5", "warn");
          }
          break;

        case 'set':
          this.handleSetCommand(arg1, arg2, arg3, parts[4]);
          break;

        case 'goto':
          if (!arg1 || !arg2 || !arg3) {
            this.printCli("Usage: goto <bot_id> <x> <y> (e.g. 'goto 1 45 20')", "warn");
          } else {
            const bot = this.resolveBot(arg1);
            const gx = parseInt(arg2, 10);
            const gy = parseInt(arg3, 10);
            if (bot) {
              bot.targetStation = null;
              bot.state = 'MOVING_TO_PICKUP';
              bot.path = [{ x: gx, y: gy }];
              bot.pathIndex = 0;
              this.printCli(`Dispatched ${bot.id} directly to (${gx}, ${gy}).`, "success");
            }
          }
          break;

        case 'add':
        case 'spawn':
          if (!arg1) {
            this.printCli("Usage: add <amr | npc | rack | parcel | hurdle | cart> <x> <y>", "warn");
          } else {
            const sx = parts[2] ? parseInt(parts[2], 10) : null;
            const sy = parts[3] ? parseInt(parts[3], 10) : null;
            if (arg1 === 'amr' || arg1 === 'bot') registerAndSpawnAmr(sx, sy);
            else if (arg1 === 'female') registerAndSpawnHuman(sx, sy, 'female');
            else if (arg1 === 'male' || arg1 === 'worker' || arg1 === 'npc' || arg1 === 'human') {
              const gender = parts[4] === 'female' ? 'female' : 'male';
              registerAndSpawnHuman(sx, sy, gender);
            }
            else if (arg1 === 'rack' || arg1 === 'shelving') registerAndSpawnRack(sx, sy);
            else if (arg1 === 'parcel' || arg1 === 'pkg' || arg1 === 'cargo') registerAndSpawnParcel(sx, sy);
            else if (arg1 === 'hurdle' || arg1 === 'cone' || arg1 === 'obstacle') registerAndSpawnHurdle(sx, sy);
            else if (arg1 === 'cart' || arg1 === 'pallet') registerAndSpawnPalletCart(sx, sy);
            else this.printCli(`Unknown entity to add: ${arg1}. Available: amr, npc, rack, parcel, hurdle, cart.`, "error");
          }
          break;

        case 'inject':
          const cnt = parseInt(arg1 || '50', 10);
          if (typeof submitBulkIngest === 'function') {
            const inp = document.getElementById('bulk-input-val');
            if (inp) inp.value = cnt;
            submitBulkIngest();
            this.printCli(`Injected ${cnt} packages into 3D storage slots.`, "success");
          }
          break;

        case 'reset':
          window.confirmQuickReset();
          break;

        default:
          this.printCli(`Command '${verb}' not recognized. Type 'help' for manual.`, "error");
          break;
      }
    }

    handleSetCommand(attr, target, val1, val2) {
      if (!attr || !target || !val1) {
        this.printCli("Usage: set <batt|speed|pos|state> <bot_id> <value>", "warn");
        return;
      }

      const bot = this.resolveBot(target);
      if (!bot) {
        this.printCli(`Robot not found: ${target}`, "error");
        return;
      }

      switch (attr) {
        case 'batt':
        case 'battery':
          const pct = Math.max(0, Math.min(100, parseFloat(val1)));
          bot.battery = pct;
          this.printCli(`Updated ${bot.id} battery SoC to ${pct.toFixed(1)}%.`, "success");
          break;

        case 'speed':
        case 'spd':
          const spd = Math.max(0.2, Math.min(8.0, parseFloat(val1)));
          bot.speed = spd;
          this.printCli(`Updated ${bot.id} max travel speed to ${spd.toFixed(1)} m/s.`, "success");
          break;

        case 'state':
          bot.state = val1.toUpperCase();
          this.printCli(`Forced ${bot.id} operational state to ${bot.state}.`, "success");
          break;

        case 'pos':
          const px = parseInt(val1, 10);
          const py = parseInt(val2, 10);
          if (!isNaN(px) && !isNaN(py)) {
            bot.x = px;
            bot.y = py;
            bot.gridX = px;
            bot.gridY = py;
            this.printCli(`Teleported ${bot.id} to (${px}, ${py}).`, "success");
          }
          break;

        default:
          this.printCli(`Unknown attribute '${attr}'. Use batt, speed, state, or pos.`, "error");
          break;
      }
    }

    resolveBot(str) {
      if (!window.AMR_FLEET) return null;
      if (/^\\d+$/.test(str)) {
        const id = `AMR-${String(str).padStart(2, '0')}`;
        return window.AMR_FLEET.find(b => b.id.toLowerCase() === id.toLowerCase());
      }
      return window.AMR_FLEET.find(b => b.id.toLowerCase() === str.toLowerCase());
    }

    showFleetStatus(targetId) {
      if (!window.AMR_FLEET) return;
      if (targetId) {
        const b = this.resolveBot(targetId);
        if (b) {
          this.printCli(`<strong>--- AMR ${b.id} TELEMETRY ---</strong><br>
• Battery: <strong>${b.battery.toFixed(1)}%</strong><br>
• Floor: <strong>Level ${b.floor || 1}</strong><br>
• Position: <strong>(${Math.round(b.x)}, ${Math.round(b.y)})</strong><br>
• State: <strong>${b.state}</strong><br>
• Speed: <strong>${(b.currentSpeed || 0).toFixed(2)} m/s</strong>`, 'info');
        }
        return;
      }

      let tableHtml = `<div style="font-weight:700; color:#fff; margin-bottom:4px;">ACTIVE FLEET TELEMETRY MATRIX (${window.AMR_FLEET.length} UNITS):</div>`;
      tableHtml += `<table style="width:100%; font-size:10.5px; border-collapse:collapse;">
        <tr style="border-bottom:1px solid rgba(255,255,255,0.2); color:#94a3b8; text-align:left;">
          <th>ID</th><th>BATT</th><th>FLOOR</th><th>POS</th><th>STATE</th><th>CARGO</th>
        </tr>`;

      for (const b of window.AMR_FLEET) {
        const col = b.battery > 50 ? '#4ade80' : (b.battery > 20 ? '#fbbf24' : '#f87171');
        tableHtml += `
          <tr style="border-bottom:1px solid rgba(255,255,255,0.06);">
            <td style="color:#fff; font-weight:700;">${b.id}</td>
            <td style="color:${col};">${Math.round(b.battery)}%</td>
            <td>L${b.floor || 1}</td>
            <td>(${Math.round(b.x)},${Math.round(b.y)})</td>
            <td style="color:#38bdf8;">${b.state}</td>
            <td>${b.carriedParcels ? b.carriedParcels.length : 0} pkgs</td>
          </tr>`;
      }
      tableHtml += `</table>`;
      this.printCli(tableHtml, 'info');
    }

    showHelpManual(topic) {
      const top = (topic || '').toLowerCase();
      if (!top || top === 'all') {
        this.printCli(`<strong>=== EDGE-AI MISSION CONTROL CLI BOSS MANUAL ===</strong><br>
Type <strong>help &lt;segment&gt;</strong> to filter: <em>help robot</em> | <em>help nav</em> | <em>help spawn</em> | <em>help sim</em><br><br>
<strong style="color:#38bdf8;">[FLEET COMMANDS]</strong><br>
&bull; <strong>status [id]</strong>: View fleet telemetry or specific robot metrics<br>
&bull; <strong>halt [all|id]</strong>: Emergency stop AMRs (humans continue active)<br>
&bull; <strong>run [all|id]</strong>: Resume autonomous operations<br>
&bull; <strong>set batt &lt;id&gt; &lt;0-100&gt;</strong>: Modify robot battery SoC percentage<br>
&bull; <strong>set speed &lt;id&gt; &lt;val&gt;</strong>: Modify robot travel speed<br>
&bull; <strong>set state &lt;id&gt; &lt;state&gt;</strong>: Force robot state machine<br>
&bull; <strong>set pos &lt;id&gt; &lt;x&gt; &lt;y&gt;</strong>: Relocate robot instantly to grid position<br><br>
<strong style="color:#38bdf8;">[NAVIGATION &amp; CAMERA]</strong><br>
&bull; <strong>spec &lt;id&gt;</strong>: Follow AMR with 3D camera<br>
&bull; <strong>drive &lt;id|name&gt;</strong>: WASD manual tele-operation (ESC to release)<br>
&bull; <strong>elev &lt;id&gt; &lt;1|2&gt;</strong>: Dispatch AMR to Floor 1 or 2 via freight elevator<br>
&bull; <strong>goto &lt;id&gt; &lt;x&gt; &lt;y&gt;</strong>: Direct route override to target coordinates<br><br>
<strong style="color:#38bdf8;">[SPAWNING &amp; CARGO]</strong><br>
&bull; <strong>spawn amr [x y]</strong>: Spawn autonomous AMR with 3D model &amp; path<br>
&bull; <strong>spawn male [x y]</strong>: Spawn male worker operator with collision AI<br>
&bull; <strong>spawn female [x y]</strong>: Spawn female worker operator with collision AI<br>
&bull; <strong>spawn cart [x y]</strong>: Spawn pallet staging cart<br>
&bull; <strong>inject &lt;count&gt;</strong>: Ingest packages into 3D storage slots (+50, +200)<br><br>
<strong style="color:#38bdf8;">[SIMULATION &amp; SYSTEM]</strong><br>
&bull; <strong>speed &lt;0.5|1|2|5&gt;</strong>: Adjust simulation warp multiplier<br>
&bull; <strong>reset</strong>: Quick reset warehouse state to default (0123456789)<br>
&bull; <strong>clear / cls</strong>: Clear terminal screen<br>
<span style="font-size:10px; color:#94a3b8;">* Multi-statement commands supported with ';' or '&&' (e.g. 'halt all; set batt 1 100; run all')</span>`, 'info');
      } else if (top === 'robot' || top === 'bot' || top === 'fleet') {
        this.printCli(`<strong>=== CLI MANUAL: ROBOT &amp; FLEET COMMANDS ===</strong><br>
&bull; <strong>status [id]</strong>: Detailed telemetry breakdown (battery, payload, state)<br>
&bull; <strong>halt [all|id]</strong>: Stop all AMRs or specific robot (ISO 3691-4 safety)<br>
&bull; <strong>run [all|id]</strong>: Resume autonomous cruising<br>
&bull; <strong>set batt &lt;id&gt; &lt;0-100&gt;</strong>: Set robot battery SoC percentage<br>
&bull; <strong>set speed &lt;id&gt; &lt;val&gt;</strong>: Set robot travel speed in cells/sec<br>
&bull; <strong>set state &lt;id&gt; &lt;state&gt;</strong>: Force state (IDLE, MOVING, CHARGING, etc.)<br>
&bull; <strong>set pos &lt;id&gt; &lt;x&gt; &lt;y&gt;</strong>: Instant reposition to grid coordinates`, 'info');
      } else if (top === 'nav' || top === 'camera' || top === 'cam') {
        this.printCli(`<strong>=== CLI MANUAL: NAVIGATION &amp; CAMERA COMMANDS ===</strong><br>
&bull; <strong>spec &lt;id&gt;</strong>: Follow AMR in 3D orbit view<br>
&bull; <strong>drive &lt;id|name&gt;</strong>: Manual WASD tele-operation (AMR or human)<br>
&bull; <strong>elev &lt;id&gt; &lt;1|2&gt;</strong>: Dispatch AMR across Mezzanine Level 1/2 via elevator<br>
&bull; <strong>goto &lt;id&gt; &lt;x&gt; &lt;y&gt;</strong>: Order AMR directly to destination coordinates`, 'info');
      } else if (top === 'spawn' || top === 'add') {
        this.printCli(`<strong>=== CLI MANUAL: SPAWNING COMMANDS ===</strong><br>
&bull; <strong>spawn amr [x y]</strong>: Create new autonomous AMR<br>
&bull; <strong>spawn male [x y]</strong>: Spawn male operator (green vest) with collision AI<br>
&bull; <strong>spawn female [x y]</strong>: Spawn female operator (orange vest) with collision AI<br>
&bull; <strong>spawn cart [x y]</strong>: Spawn staging pallet cart<br>
&bull; <strong>inject &lt;count&gt;</strong>: Ingest packages into 3D storage slots`, 'info');
      } else if (top === 'sim' || top === 'system') {
        this.printCli(`<strong>=== CLI MANUAL: SIMULATION &amp; SYSTEM COMMANDS ===</strong><br>
&bull; <strong>speed &lt;0.5|1|2|5&gt;</strong>: Set simulation speed multiplier<br>
&bull; <strong>reset</strong>: Quick reset warehouse to default room configuration<br>
&bull; <strong>clear / cls</strong>: Clear interactive console screen`, 'info');
      } else {
        this.printCli(`Unknown segment: '${topic}'. Available: <strong>robot</strong>, <strong>nav</strong>, <strong>spawn</strong>, <strong>sim</strong>, or <strong>all</strong>.`, 'warn');
      }
    }
  }

  const terminalBoss = new CommandTerminalBoss();
  window.terminalBoss = terminalBoss;

  // =========================================================================
  // 8. NATURAL HUMAN CURVATURE CAPTCHA
  // =========================================================================
  class HumanMotionCaptcha {
    constructor() {
      this.points = [];
      this.isVerified = false;
      this.lastSample = Date.now();

      window.addEventListener('mousemove', (e) => {
        const now = Date.now();
        if (now - this.lastSample > 20) {
          this.points.push({ x: e.clientX, y: e.clientY, t: now });
          if (this.points.length > 40) this.points.shift();
          this.lastSample = now;
        }
      });
    }

    testCurvature() {
      if (this.points.length < 4) return true;
      let curvatureSum = 0;
      for (let i = 2; i < this.points.length; i++) {
        const p0 = this.points[i - 2];
        const p1 = this.points[i - 1];
        const p2 = this.points[i];
        const a1 = Math.atan2(p1.y - p0.y, p1.x - p0.x);
        const a2 = Math.atan2(p2.y - p1.y, p2.x - p1.x);
        curvatureSum += Math.abs(a2 - a1);
      }
      return curvatureSum > 0.04;
    }

    verify(callback) {
      if (this.isVerified) {
        callback(true);
        return;
      }
      const passed = this.testCurvature();
      setTimeout(() => {
        this.isVerified = true;
        callback(passed);
      }, 400);
    }
  }

  const humanCaptcha = new HumanMotionCaptcha();
  window.humanCaptcha = humanCaptcha;

  // =========================================================================
  // 9. ROOM ACCESS & OFFLINE BACKGROUND CATCHUP
  // =========================================================================
  class WarehouseRoomManager {
    constructor() {
      this.currentRoom = '0123456789';
    }

    init() {
      const saved = localStorage.getItem('amr_active_room');
      if (saved && /^\\d{10}$/.test(saved)) {
        this.currentRoom = saved;
      }
      this.updateHeaderBadge();
      this.checkOfflineCatchup();
    }

    updateHeaderBadge() {
      const el = document.getElementById('header-room-id');
      if (el) el.textContent = `#${this.currentRoom}`;
    }

    checkOfflineCatchup() {
      const key = `amr_room_ts_${this.currentRoom}`;
      const last = localStorage.getItem(key);
      const now = Date.now();
      localStorage.setItem(key, String(now));

      if (last) {
        const elapsedSec = Math.max(0, Math.min(86400, (now - parseInt(last, 10)) / 1000));
        if (elapsedSec > 4) {
          const completedOrders = Math.floor(elapsedSec / 25);
          setTimeout(() => {
            if (typeof logTerminal === 'function') {
              logTerminal('SYSTEM', 'tag-overtake', `[SYNC] Reconnected to Room #${this.currentRoom}. Background Execution Catchup: ${Math.round(elapsedSec)}s delta simulated (${completedOrders} order tasks completed).`);
            }
          }, 1200);
        }
      }
    }

    switchRoom(roomId) {
      if (!/^\\d{10}$/.test(roomId)) {
        alert("Please enter a valid 10-digit Warehouse Room ID (e.g. 0123456789).");
        return false;
      }
      this.currentRoom = roomId;
      localStorage.setItem('amr_active_room', roomId);
      localStorage.setItem(`amr_room_ts_${roomId}`, String(Date.now()));
      sessionStorage.setItem('amr_warehouse_verified', 'true');
      this.updateHeaderBadge();
      if (typeof logTerminal === 'function') {
        logTerminal('SYSTEM', 'tag-traffic', `[ROOM] Switched active warehouse session to #${roomId}.`);
      }
      return true;
    }
  }

  const roomManager = new WarehouseRoomManager();
  window.roomManager = roomManager;

  // =========================================================================
  // 10. 2-LEVEL MEZZANINE DECK, 2 STEEL STAIRS & FREIGHT ELEVATOR (3D)
  // =========================================================================
  let elevatorCarriageMesh = null;
  let elevatorState = {
    x: 40,
    y: 25,
    currentFloor: 1,
    targetFloor: 1,
    carriageY: 0.1,
    isMoving: false,
    passengerBot: null
  };

  function setup3DMezzanineAndElevator() {
    // Single-level industrial layout (1 Floor / 1 Level)
  }

  function update3DElevator(dt) {
    // Single-level industrial layout
  }

  function dispatchAmrToFloor(botId, targetFloor) {
    if (window.terminalBoss) {
      window.terminalBoss.printCli("Warehouse operates on a unified single-level industrial layout (1 Floor).", "info");
    }
  }

  window.dispatchAmrToFloor = dispatchAmrToFloor;

  // =========================================================================
  // 11. HUMAN WORKERS WITH REAL GRID COLLISION AI
  // =========================================================================
  function isCellWalkable(gx, gy, selfId = null) {
    if (!window.mapData) return true;
    const w = window.mapData.width || 80;
    const h = window.mapData.height || 50;

    // 1. Boundary check with perimeter margin
    if (gx < 1.0 || gx > w - 2.0 || gy < 1.0 || gy > h - 2.0) return false;

    // 2. Exact Rack Collision: checks actual distance to rack bounding box!
    // Aisle is 1.0 cell wide. Rack box occupies [rx - 0.5, rx + 0.5] x [ry - 0.5, ry + 0.5].
    // With clearance threshold 0.22, robot center can move freely within a 0.56-wide path down the aisle!
    if (window.mapData.grid) {
      const minRx = Math.max(0, Math.floor(gx - 1.5));
      const maxRx = Math.min(w - 1, Math.ceil(gx + 1.5));
      const minRy = Math.max(0, Math.floor(gy - 1.5));
      const maxRy = Math.min(h - 1, Math.ceil(gy + 1.5));

      for (let rx = minRx; rx <= maxRx; rx++) {
        for (let ry = minRy; ry <= maxRy; ry++) {
          if (window.mapData.grid[rx] && window.mapData.grid[rx][ry] === 1) {
            const cx = Math.max(rx - 0.5, Math.min(rx + 0.5, gx));
            const cy = Math.max(ry - 0.5, Math.min(ry + 0.5, gy));
            const dist = Math.hypot(gx - cx, gy - cy);
            if (dist < 0.22) {
              return false; // Blocks penetration into rack
            }
          }
        }
      }
    }

    // 3. Other AMRs: Solid collision (bots NEVER pass through each other)
    if (window.AMR_FLEET) {
      for (const bot of window.AMR_FLEET) {
        if (selfId && bot.id.toLowerCase() === selfId.toLowerCase()) continue;
        const d = Math.hypot(bot.x - gx, bot.y - gy);
        if (d < 0.85) return false;
      }
    }

    // 4. Dynamic Obstacles, Human Workers & Dropped Boxes: Solid collision
    if (window.DYNAMIC_OBSTACLES) {
      for (const obs of window.DYNAMIC_OBSTACLES) {
        if (selfId && (obs.id === selfId || obs.name === selfId)) continue;
        // If this box was just dropped by this robot, allow grace period to drive away cleanly!
        if (obs.droppedByBotId === selfId && (obs.dropGraceTimer || 0) > 0) continue;
        const d = Math.hypot(obs.x - gx, obs.y - gy);
        if (d < 0.80) return false;
      }
    }

    return true;
  }

  function updateHumanWorkersWithCollision(dt) {
    if (!window.DYNAMIC_OBSTACLES) return;

    for (const obs of window.DYNAMIC_OBSTACLES) {
      if (obs.type !== 'human' || obs.manualOverride) continue;
      if (!obs.route || obs.route.length === 0) continue;

      const wp = obs.route[obs.routeIndex];
      const dx = wp.x - obs.x;
      const dy = wp.y - obs.y;
      const dist = Math.hypot(dx, dy);

      if (dist < 0.2) {
        obs.routeIndex = (obs.routeIndex + 1) % obs.route.length;
      } else {
        const step = Math.min(dist, obs.speed * (window.simSpeed || 1.0) * dt);
        const vx = (dx / dist) * step;
        const vy = (dy / dist) * step;

        const nextX = obs.x + vx;
        const nextY = obs.y + vy;

        if (isCellWalkable(nextX, nextY)) {
          obs.x = nextX;
          obs.y = nextY;
          obs.heading = Math.atan2(dy, dx);
        } else {
          obs.routeIndex = (obs.routeIndex + 1) % obs.route.length;
        }
      }
    }
  }

  // =========================================================================
  // 12. MANUAL WASD TELE-OPERATION (AMR & WORKER)
  // Video-Game Responsive Physics + 3 Camera Modes (V) + Cargo Pick/Drop (E)
  // =========================================================================
  let manualTarget = null;
  let manualCamMode = 'tpv'; // 'tpv' (3rd person), 'closeup' (hood/cockpit), 'free' (free orbit)
  let manual2DLocked = true;
  const activeKeys = { w: false, a: false, s: false, d: false, brake: false };

  function handleCargoPickDrop() {
    if (!manualTarget || !manualTarget.ref || manualTarget.type !== 'robot') return;
    const bot = manualTarget.ref;
    const isCarrying = Boolean(bot.isLoadedYellow || (bot.carriedParcels && bot.carriedParcels.length > 0) || (bot.cargo && typeof bot.cargo === 'object' && Object.keys(bot.cargo).length > 0) || (bot.orderBox && bot.orderBox.items && bot.orderBox.items.length > 0));

    if (isCarrying) {
      // 1. Check if dropped near a rack: box goes inside the rack shelf!
      let shelvedInRack = false;
      if (window.rackMemory) {
        const bx = Math.round(bot.x);
        const by = Math.round(bot.y);
        const neighbors = [
          [bx, by - 1], [bx, by + 1], [bx - 1, by], [bx + 1, by]
        ];
        for (const [rx, ry] of neighbors) {
          const rKey = `${rx},${ry}`;
          const rack = window.rackMemory[rKey];
          if (rack && rack.floors) {
            // Find lowest empty tier
            for (let f = 0; f < 5; f++) {
              if (rack.floors[f] === null) {
                const pkgId = `PKG-${Math.floor(1000 + Math.random() * 9000)}`;
                rack.floors[f] = bot.cargo || {
                  parcel_id: pkgId,
                  sku: rack.categorySku || 'SKU-GEN',
                  name: rack.categoryName || 'General Storage',
                  weight: '14.5kg'
                };
                shelvedInRack = true;
                bot.isLoadedYellow = false;
                bot.cargo = null;
                bot.orderBox = null;
                bot.carriedParcels = [];
                if (typeof window.update3DRacksTotes === 'function') {
                  window.update3DRacksTotes();
                }
                if (window.terminalBoss) {
                  window.terminalBoss.printCli(`[RACK DEPOSIT] ${bot.id} placed yellow parcel carton into Rack (${rx}, ${ry}) Tier ${f + 1}. Scissor-lift lowered.`, 'success');
                }
                break;
              }
            }
            if (shelvedInRack) break;
          }
        }
      }

      // 2. If not adjacent to a rack, drop onto the warehouse floor
      if (!shelvedInRack) {
        bot.isLoadedYellow = false;
        bot.cargo = null;
        bot.orderBox = null;
        bot.carriedParcels = [];
        const dropX = Math.round(bot.x);
        const dropY = Math.round(bot.y);
        let newBox = null;
        if (typeof window.spawnDroppedParcelBox === 'function') {
          newBox = window.spawnDroppedParcelBox(dropX, dropY);
        } else if (typeof window.spawnPalletObstacle === 'function') {
          newBox = window.spawnPalletObstacle(dropX, dropY);
        }
        if (newBox) {
          newBox.droppedByBotId = bot.id;
          newBox.dropGraceTimer = 3.5; // Bot has 3.5s grace period to drive away without collision
        }
        if (window.terminalBoss) {
          window.terminalBoss.printCli(`[CARGO] ${bot.id} deposited yellow parcel carton at (${dropX}, ${dropY}). Scissor-lift lowered.`, 'success');
        }
      }
    } else {
      // PICK CARGO from floor box or adjacent rack
      let picked = false;
      // 1. Pick from dropped floor box
      if (window.DYNAMIC_OBSTACLES) {
        const boxIdx = window.DYNAMIC_OBSTACLES.findIndex(o => (o.type === 'parcel_box' || o.type === 'pallet_cart') && Math.hypot(o.x - bot.x, o.y - bot.y) <= 1.85);
        if (boxIdx !== -1) {
          const removedBox = window.DYNAMIC_OBSTACLES.splice(boxIdx, 1)[0];
          if (window.obstacleModels3D && window.obstacleModels3D[removedBox.id] && window.scene3D) {
            window.scene3D.remove(window.obstacleModels3D[removedBox.id].root);
            delete window.obstacleModels3D[removedBox.id];
          }
          bot.isLoadedYellow = true;
          bot.cargo = { sku: 'SKU-YELLOW-PKG', weightKg: 12.0 };
          bot.carriedParcels = [{ sku: 'SKU-YELLOW-PKG', weightKg: 12.0 }];
          picked = true;
          if (window.terminalBoss) {
            window.terminalBoss.printCli(`[CARGO] ${bot.id} picked up floor box at (${Math.round(removedBox.x)}, ${Math.round(removedBox.y)}). Scissor-lift elevated.`, 'success');
          }
        }
      }

      // 2. Pick from adjacent rack shelf
      if (!picked && window.rackMemory) {
        const bx = Math.round(bot.x);
        const by = Math.round(bot.y);
        const neighbors = [
          [bx, by - 1], [bx, by + 1], [bx - 1, by], [bx + 1, by]
        ];
        for (const [rx, ry] of neighbors) {
          const rKey = `${rx},${ry}`;
          const rack = window.rackMemory[rKey];
          if (rack && rack.floors) {
            for (let f = 4; f >= 0; f--) {
              if (rack.floors[f]) {
                const item = rack.floors[f];
                rack.floors[f] = null; // Visually disappears from rack
                bot.isLoadedYellow = true;
                bot.cargo = item;
                bot.carriedParcels = [item];
                picked = true;
                if (typeof window.update3DRacksTotes === 'function') {
                  window.update3DRacksTotes();
                }
                if (window.terminalBoss) {
                  window.terminalBoss.printCli(`[CARGO] ${bot.id} picked yellow parcel from Rack (${rx}, ${ry}) Tier ${f + 1}. Scissor-lift elevated.`, 'success');
                }
                break;
              }
            }
            if (picked) break;
          }
        }
      }

      // 3. Fallback: warn if no cargo in reach (NO INFINITE CARGO OUT OF THIN AIR)
      if (!picked) {
        if (window.terminalBoss) {
          window.terminalBoss.printCli(`[CARGO] No parcel cartons or rack items within reach of ${bot.id}. Drive closer to a box or rack shelf.`, 'warn');
        }
      }
    }
    if (typeof window.render === 'function') window.render();
    updateChargeAndCargoPrompts();
  }

  function handleDockAndCharge(portId) {
    if (!manualTarget || !manualTarget.ref || manualTarget.type !== 'robot') return;
    const bot = manualTarget.ref;
    releaseManualControl();
    if (typeof window.dockAtCharger === 'function') {
      window.dockAtCharger(portId, bot.id);
      bot.state = 'IDLE_CHARGING';
      bot.targetDesc = `Fast Charging at ${portId}`;
      if (window.terminalBoss) {
        window.terminalBoss.printCli(`[CHARGER] ${bot.id} docked into ${portId}. Fast charging active.`, 'success');
      }
    }
  }
  window.handleDockAndCharge = handleDockAndCharge;
  window.handleCargoPickDrop = handleCargoPickDrop;

  function updateChargeAndCargoPrompts() {
    const promptContainer = document.getElementById('manual-dynamic-prompts');
    if (!promptContainer) return;
    if (!manualTarget || !manualTarget.ref || manualTarget.type !== 'robot') {
      promptContainer.innerHTML = '';
      return;
    }
    const bot = manualTarget.ref;
    let html = '';

    // Check proximity to Charging Stations (distance <= 1.85)
    if (window.CHARGING_PORTS) {
      const nearPort = window.CHARGING_PORTS.find(p => Math.hypot(p.x - bot.x, p.y - bot.y) <= 1.85);
      if (nearPort) {
        html += `<button class="mc-prompt-btn charge" onclick="handleDockAndCharge('${nearPort.id}')">
          <svg viewBox="0 0 24 24" width="11" height="11" stroke="currentColor" stroke-width="2" fill="none"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
          Dock & Charge (${nearPort.id})
        </button>`;
      }
    }

    // Check proximity to Racks or Floor Boxes for Pick / Drop (Zero Emojis!)
    const isCarrying = Boolean(bot.isLoadedYellow || (bot.carriedParcels && bot.carriedParcels.length > 0) || (bot.cargo && typeof bot.cargo === 'object' && Object.keys(bot.cargo).length > 0) || (bot.orderBox && bot.orderBox.items && bot.orderBox.items.length > 0));
    const boxSvg = `<svg viewBox="0 0 24 24" width="12" height="12" stroke="currentColor" stroke-width="2" fill="none"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>`;

    if (isCarrying) {
      html += `<button class="mc-prompt-btn drop" onclick="handleCargoPickDrop()">
        ${boxSvg}
        [E] Drop Box
      </button>`;
    } else {
      let nearPickable = false;
      if (window.DYNAMIC_OBSTACLES && window.DYNAMIC_OBSTACLES.some(o => (o.type === 'parcel_box' || o.type === 'pallet_cart') && Math.hypot(o.x - bot.x, o.y - bot.y) <= 1.85)) {
        nearPickable = true;
      }
      if (!nearPickable && window.rackMemory) {
        const bx = Math.round(bot.x), by = Math.round(bot.y);
        for (const [rx, ry] of [[bx, by - 1], [bx, by + 1], [bx - 1, by], [bx + 1, by]]) {
          const rk = window.rackMemory[`${rx},${ry}`];
          if (rk && rk.floors && rk.floors.some(f => f !== null)) { nearPickable = true; break; }
        }
      }
      if (nearPickable) {
        html += `<button class="mc-prompt-btn pick" onclick="handleCargoPickDrop()">
          ${boxSvg}
          [E] Pick Box
        </button>`;
      }
    }

    promptContainer.innerHTML = html;
  }

  function initManualControlListeners() {
    window.addEventListener('keydown', (e) => {
      if (document.activeElement && (document.activeElement.tagName === 'INPUT' || document.activeElement.tagName === 'TEXTAREA')) {
        return;
      }
      const key = e.key.toLowerCase();

      // Cycle camera modes on 'V'
      if (key === 'v') {
        if (manualTarget && manualTarget.ref) {
          e.preventDefault();
          if (window.viewMode === '2D') {
            // In 2D: toggle between locked camera follow and free look
            manual2DLocked = !manual2DLocked;
            const camLabel = document.getElementById('manual-cam-mode-lbl');
            if (manual2DLocked) {
              window.trackedRobotId = manualTarget.ref.id;
              window.trackCameraFollow = true;
              if (typeof window.zoomToScale === 'function') window.zoomToScale(28);
              if (camLabel) camLabel.textContent = '2D LOCKED';
            } else {
              window.trackCameraFollow = false;
              if (typeof window.stopTrackingBot === 'function') window.stopTrackingBot();
              if (camLabel) camLabel.textContent = '2D FREE';
            }
          } else {
            // In 3D: cycle 3RD PERSON -> CLOSE UP -> FREE MOVE
            if (manualCamMode === 'tpv') {
              manualCamMode = 'closeup';
            } else if (manualCamMode === 'closeup') {
              manualCamMode = 'free';
            } else {
              manualCamMode = 'tpv';
            }
            const camLabel = document.getElementById('manual-cam-mode-lbl');
            if (camLabel) {
              camLabel.textContent = manualCamMode === 'tpv' ? '3RD PERSON' : (manualCamMode === 'closeup' ? 'CLOSE UP' : 'FREE MOVE');
            }
          }
          if (window.terminalBoss) {
            window.terminalBoss.printCli(`[CAM] Manual view mode toggled`, 'info');
          }
        }
        return;
      }

      // Pick / Drop Cargo on 'E' (or 'F')
      if (key === 'e' || key === 'f') {
        if (manualTarget && manualTarget.ref && manualTarget.type === 'robot') {
          e.preventDefault();
          handleCargoPickDrop();
        }
        return;
      }

      // Quick Charge on 'C'
      if (key === 'c') {
        if (manualTarget && manualTarget.ref && manualTarget.type === 'robot' && window.CHARGING_PORTS) {
          const nearPort = window.CHARGING_PORTS.find(p => Math.hypot(p.x - manualTarget.ref.x, p.y - manualTarget.ref.y) <= 2.0);
          if (nearPort) {
            e.preventDefault();
            handleDockAndCharge(nearPort.id);
            return;
          }
        }
      }

      if (!manualTarget) return;

      if (key === 'w' || key === 'arrowup') { activeKeys.w = true; e.preventDefault(); }
      if (key === 's' || key === 'arrowdown') { activeKeys.s = true; e.preventDefault(); }
      if (key === 'a' || key === 'arrowleft') { activeKeys.a = true; e.preventDefault(); }
      if (key === 'd' || key === 'arrowright') { activeKeys.d = true; e.preventDefault(); }
      if (key === ' ') { activeKeys.brake = true; e.preventDefault(); }
      if (key === 'escape') { releaseManualControl(); e.preventDefault(); }
    });

    window.addEventListener('keyup', (e) => {
      const key = e.key.toLowerCase();
      if (key === 'w' || key === 'arrowup') activeKeys.w = false;
      if (key === 's' || key === 'arrowdown') activeKeys.s = false;
      if (key === 'a' || key === 'arrowleft') activeKeys.a = false;
      if (key === 'd' || key === 'arrowright') activeKeys.d = false;
      if (key === ' ') activeKeys.brake = false;
    });
  }

  function setManualControl(type, id) {
    // If Emergency Fleet Halt is active, disallow manual tele-operation (ISO 3691-4)
    if (window.fleetHalted) {
      if (window.terminalBoss) {
        window.terminalBoss.printCli(`[HALT LOCKED] Manual tele-operation is locked during Emergency Fleet Halt (ISO 3691-4).`, 'error');
      }
      alert('Emergency Fleet Halt is Active! Manual tele-operation is locked until fleet halt is released.');
      return;
    }

    let entity = null;
    if (type === 'robot' && window.AMR_FLEET) {
      entity = window.AMR_FLEET.find(b => b.id.toLowerCase() === id.toLowerCase());
    } else if (type === 'human' && window.DYNAMIC_OBSTACLES) {
      entity = window.DYNAMIC_OBSTACLES.find(h => h.id.toLowerCase() === id.toLowerCase() || h.name.toLowerCase() === id.toLowerCase());
    }

    if (!entity) return;
    if (manualTarget && manualTarget.ref) {
      manualTarget.ref.manualOverride = false;
      manualTarget.ref.currentSpeed = 0;
    }

    manualTarget = { type, ref: entity };
    entity.manualOverride = true;

    // Clear autonomous queue paths so motor never fights user
    entity.path = [];
    entity.pathIndex = 0;
    entity.isWaiting = false;
    entity.isBackingUp = false;
    entity.isSideStepping = false;
    entity.yieldTo = null;
    entity.savedDest = null;
    entity.currentSpeed = 0;
    manualCamMode = 'tpv';
    manual2DLocked = true;

    if (window.viewMode === '2D') {
      window.trackedRobotId = entity.id;
      window.trackCameraFollow = true;
      if (typeof window.zoomToScale === 'function') window.zoomToScale(28);
    }

    const overlay = document.getElementById('manual-ctrl-overlay');
    if (overlay) {
      overlay.style.display = 'flex';
      const label = document.getElementById('manual-ctrl-target-name');
      if (label) label.textContent = `${type.toUpperCase()}: ${entity.name || entity.id}`;
      const camLabel = document.getElementById('manual-cam-mode-lbl');
      if (camLabel) camLabel.textContent = window.viewMode === '2D' ? '2D LOCKED' : '3RD PERSON';
    }

    if (window.terminalBoss) {
      window.terminalBoss.printCli(`[TELE-OP] Manual control engaged for ${entity.name || entity.id}. WASD to drive, E to pick/drop box, V for camera lock.`, 'success');
    }
    updateChargeAndCargoPrompts();
  }

  function releaseManualControl() {
    if (manualTarget && manualTarget.ref) {
      manualTarget.ref.manualOverride = false;
      manualTarget.ref.currentSpeed = 0;
      manualTarget.ref.path = [];
    }
    manualTarget = null;
    manual2DLocked = false;
    window.trackCameraFollow = false;
    if (typeof window.stopTrackingBot === 'function') {
      window.stopTrackingBot();
    }
    const overlay = document.getElementById('manual-ctrl-overlay');
    if (overlay) overlay.style.display = 'none';
    const promptContainer = document.getElementById('manual-dynamic-prompts');
    if (promptContainer) promptContainer.innerHTML = '';
    if (window.terminalBoss) {
      window.terminalBoss.printCli(`[TELE-OP] Manual control released.`, 'info');
    }
  }

  function updateManualControl(dt) {
    if (!manualTarget || !manualTarget.ref) return;

    // Emergency halt lock
    if (window.fleetHalted) {
      manualTarget.ref.currentSpeed = 0;
      releaseManualControl();
      return;
    }

    const ent = manualTarget.ref;
    const isRobot = manualTarget.type === 'robot';

    // Battery decreases when driving in manual mode!
    if (isRobot) {
      const drainRate = Math.abs(ent.currentSpeed || 0) > 0.1 ? 0.35 : 0.05;
      ent.battery = Math.max(0, (ent.battery || 100) - drainRate * dt * (window.simSpeed || 1.0));
      if (ent.battery <= 0) {
        ent.battery = 0;
        ent.state = 'OUT_OF_CHARGE';
        ent.currentSpeed = 0;
        const botId = ent.id;
        releaseManualControl();
        if (window.terminalBoss) {
          window.terminalBoss.printCli(`[BATTERY DEPLETED] ${botId} reached 0% battery. Autonomous AGV recovery tug dispatched.`, 'error');
        }
        if (typeof window.rescueStrandedBot === 'function') {
          window.rescueStrandedBot(botId);
        }
        return;
      }
    }

    // Video Game Handling Characteristics
    const maxForward = isRobot ? 3.8 : 2.2;
    const maxReverse = isRobot ? 2.0 : 1.3;
    const accelRate  = isRobot ? 9.0 : 11.0;
    const decelRate  = isRobot ? 12.0 : 16.0;
    const turnRate   = isRobot ? 3.4 : 3.8;

    // STEERING CORRECTION:
    // A turns LEFT (decrease heading in 3D / 2D convention)
    // D turns RIGHT (increase heading in 3D / 2D convention)
    if (activeKeys.a) {
      ent.heading = (ent.heading || 0) - turnRate * dt;
    }
    if (activeKeys.d) {
      ent.heading = (ent.heading || 0) + turnRate * dt;
    }
    while (ent.heading > Math.PI) ent.heading -= 2 * Math.PI;
    while (ent.heading < -Math.PI) ent.heading += 2 * Math.PI;

    // Throttle / Brake / Coasting (W / S / SPACE)
    ent.currentSpeed = ent.currentSpeed || 0;
    if (activeKeys.brake) {
      ent.currentSpeed = 0;
    } else if (activeKeys.w) {
      ent.currentSpeed = Math.min(ent.currentSpeed + accelRate * dt, maxForward);
    } else if (activeKeys.s) {
      ent.currentSpeed = Math.max(ent.currentSpeed - accelRate * dt, -maxReverse);
    } else {
      if (ent.currentSpeed > 0) {
        ent.currentSpeed = Math.max(0, ent.currentSpeed - decelRate * dt);
      } else if (ent.currentSpeed < 0) {
        ent.currentSpeed = Math.min(0, ent.currentSpeed + decelRate * dt);
      }
    }

    // Kinematic motion step with watertight rack & entity collision
    if (Math.abs(ent.currentSpeed) > 0.001) {
      const step = ent.currentSpeed * dt;
      const cosH = Math.cos(ent.heading);
      const sinH = Math.sin(ent.heading);
      const nextX = ent.x + cosH * step;
      const nextY = ent.y + sinH * step;

      if (isCellWalkable(nextX, nextY, ent.id)) {
        ent.x = nextX;
        ent.y = nextY;
      } else if (isCellWalkable(nextX, ent.y, ent.id)) {
        // Wall/rack slide along X
        ent.x = nextX;
      } else if (isCellWalkable(ent.x, nextY, ent.id)) {
        // Wall/rack slide along Y
        ent.y = nextY;
      } else {
        ent.currentSpeed = 0; // Solid contact stop
      }
    }

    ent.gridX = Math.round(ent.x);
    ent.gridY = Math.round(ent.y);

    if (!isRobot) {
      ent.currentAction = Math.abs(ent.currentSpeed) > 0.05 ? 'Manual Walk' : 'Manual Standby';
    }

    // Update floating prompts (Dock & Charge / Pick / Drop)
    updateChargeAndCargoPrompts();

    // -------------------------------------------------------------------------
    // 3D Camera Modes in Manual Control: TPV, CLOSE UP, FREE
    // -------------------------------------------------------------------------
    if (window.camera3D && window.controls3D && window.viewMode === '3D') {
      const gridTo3D = window.gridTo3D || ((gx, gy, elev = 0) => ({
        x: (gx - (window.mapData?.width || 80) / 2 + 0.5) * (window.C_SIZE || 1.8),
        y: elev,
        z: (gy - (window.mapData?.height || 50) / 2 + 0.5) * (window.C_SIZE || 1.8)
      }));

      const pos = gridTo3D(ent.x, ent.y, 0.4);
      const dirX = Math.cos(ent.heading);
      const dirZ = Math.sin(ent.heading);

      if (manualCamMode === 'tpv') {
        const camTarget = new THREE.Vector3(
          pos.x - dirX * 5.8,
          3.6,
          pos.z - dirZ * 5.8
        );
        window.camera3D.position.lerp(camTarget, 0.12);
        window.controls3D.target.lerp(new THREE.Vector3(pos.x + dirX * 2.5, 0.5, pos.z + dirZ * 2.5), 0.14);
        window.controls3D.update();
      } else if (manualCamMode === 'closeup') {
        const camTarget = new THREE.Vector3(
          pos.x + dirX * 0.4,
          isRobot ? 0.95 : 1.6,
          pos.z + dirZ * 0.4
        );
        window.camera3D.position.lerp(camTarget, 0.16);
        window.controls3D.target.lerp(new THREE.Vector3(pos.x + dirX * 6.0, 0.8, pos.z + dirZ * 6.0), 0.18);
        window.controls3D.update();
      } else if (manualCamMode === 'free') {
        window.controls3D.target.lerp(new THREE.Vector3(pos.x, 0.5, pos.z), 0.08);
        window.controls3D.update();
      }
    }
  }

  window.setManualControl = setManualControl;
  window.releaseManualControl = releaseManualControl;

  // =========================================================================
  // 13. DRAGGABLE WINDOWS HELPER
  // =========================================================================
  function makeDraggable(element, handle) {
    if (!element || !handle) return;
    let pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;

    handle.onmousedown = dragMouseDown;

    function dragMouseDown(e) {
      e.preventDefault();
      pos3 = e.clientX;
      pos4 = e.clientY;
      document.onmouseup = closeDragElement;
      document.onmousemove = elementDrag;
    }

    function elementDrag(e) {
      e.preventDefault();
      pos1 = pos3 - e.clientX;
      pos2 = pos4 - e.clientY;
      pos3 = e.clientX;
      pos4 = e.clientY;
      element.style.top = (element.offsetTop - pos2) + "px";
      element.style.left = (element.offsetLeft - pos1) + "px";
      element.style.right = 'auto';
      element.style.bottom = 'auto';
    }

    function closeDragElement() {
      document.onmouseup = null;
      document.onmousemove = null;
    }
  }

  window.makeDraggable = makeDraggable;

  // =========================================================================
  // 14. MODAL DIALOGS CREATION (ROOM, GUIDE, CONFIRM, CONTEXT)
  // =========================================================================
  function createUIModals() {
    const roomModalHtml = `
      <div class="mc-modal-backdrop" id="modal-room-switch">
        <div class="mc-modal-card">
          <div class="mc-modal-header draggable-handle">
            <strong style="color:#fff; font-size:13px; display:flex; align-items:center; gap:8px;">
              ${SVG.robot} WAREHOUSE ROOM ACCESS
            </strong>
            <button class="track-ctrl-close-btn" onclick="closeRoomModal()">&times;</button>
          </div>
          <div class="mc-modal-body">
            <p style="font-size:12px; margin-bottom:12px; color:#94a3b8;">
              Enter your 10-Digit Warehouse Room ID to synchronize autonomous edge robots, or generate a fresh warehouse.
            </p>
            <div style="display:flex; gap:8px; margin-bottom:14px;">
              <input type="text" id="input-room-id" value="0123456789" maxlength="10" 
                style="flex:1; background:#090c12; border:1px solid rgba(255,255,255,0.2); padding:8px 12px; border-radius:6px; color:#fff; font-size:14px; font-family:monospace; font-weight:700;" />
              <button class="dropdown-trigger-btn highlight" onclick="generateRandomRoomId()">Generate ID</button>
            </div>

            <!-- Modern Security Verification Widget -->
            <div class="natural-captcha-widget" id="captcha-container" onclick="handleCaptchaClick()">
              <div style="display:flex; align-items:center; gap:14px;">
                <div class="captcha-checkbox" id="captcha-check-box">
                  <svg id="captcha-check-svg" viewBox="0 0 24 24" width="16" height="16" stroke="#ffffff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" fill="none" style="display:none;">
                    <polyline points="20 6 9 17 4 12"></polyline>
                  </svg>
                </div>
                <div>
                  <div style="font-weight:700; color:#f8fafc; font-size:13px; letter-spacing:0.2px;">I'm not a robot</div>
                  <div style="font-size:11px; color:#64748b;" id="captcha-desc-text">Operator Security Verification</div>
                </div>
              </div>
              <div style="display:flex; flex-direction:column; align-items:center; opacity:0.85;">
                <svg viewBox="0 0 24 24" width="22" height="22" stroke="#38bdf8" stroke-width="1.8" fill="none">
                  <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
                </svg>
                <span style="font-size:8px; font-family:monospace; color:#94a3b8; font-weight:700; margin-top:2px;">BEL SECURE</span>
              </div>
            </div>

            <div style="display:flex; justify-content:space-between; margin-top:10px; font-size:11px;">
              <a href="#" style="color:#38bdf8; text-decoration:none;" onclick="loadTestRoom0123(); return false;">&bull; Load Default BEL Room (0123456789)</a>
            </div>
          </div>
          <div class="mc-modal-footer">
            <button class="dropdown-trigger-btn" onclick="closeRoomModal()">Cancel</button>
            <button class="dropdown-trigger-btn highlight" id="btn-enter-room" onclick="submitRoomSwitch()">Enter Warehouse</button>
          </div>
        </div>
      </div>
    `;

    const guideModalHtml = `
      <div class="mc-modal-backdrop" id="modal-guide-about"></div>
    `;

    const confirmModalHtml = `
      <div class="mc-modal-backdrop" id="modal-confirm-warning">
        <div class="mc-modal-card" style="width:420px;">
          <div class="mc-modal-header draggable-handle">
            <strong style="color:#f87171; font-size:13px; display:flex; align-items:center; gap:8px;">
              ${SVG.alert} CRITICAL ACTION CONFIRMATION
            </strong>
            <button class="track-ctrl-close-btn" onclick="closeConfirmModal()">&times;</button>
          </div>
          <div class="mc-modal-body" id="confirm-modal-text">
            Are you sure you want to execute this action?
          </div>
          <div class="mc-modal-footer">
            <button class="dropdown-trigger-btn" onclick="closeConfirmModal()">Cancel</button>
            <button class="dropdown-trigger-btn" id="btn-confirm-action" style="background:#ef4444; border-color:#ef4444; color:#fff;" onclick="executeConfirmedAction()">Proceed</button>
          </div>
        </div>
      </div>
    `;

    const manualOverlayHtml = `
      <div id="manual-ctrl-overlay">
        <div style="display:flex; align-items:center; gap:8px;">
          <div style="width:8px; height:8px; border-radius:50%; background:#10b981; box-shadow:0 0 8px #10b981;"></div>
          <strong id="manual-ctrl-target-name" style="color:#fff; font-size:12px;">MANUAL TELE-OP</strong>
        </div>
        <div style="display:flex; gap:6px; align-items:center;">
          <span class="manual-key-badge">W</span>
          <span class="manual-key-badge">A</span>
          <span class="manual-key-badge">S</span>
          <span class="manual-key-badge">D</span>
          <span style="font-size:11px; color:#94a3b8; margin-left:2px;">Drive/Walk</span>
        </div>
        <div style="display:flex; gap:6px; align-items:center;">
          <span class="manual-key-badge">SPACE</span>
          <span style="font-size:11px; color:#94a3b8;">Brake</span>
        </div>
        <div style="display:flex; gap:6px; align-items:center;">
          <span class="manual-key-badge">E</span>
          <span style="font-size:11px; color:#94a3b8;">Pick / Drop</span>
        </div>
        <div style="display:flex; gap:6px; align-items:center;">
          <span class="manual-key-badge">V</span>
          <span style="font-size:11px; color:#38bdf8; font-weight:600;" id="manual-cam-mode-lbl">3RD PERSON</span>
        </div>
        <div id="manual-dynamic-prompts" style="display:flex; gap:6px; align-items:center;"></div>
        <button class="dropdown-trigger-btn highlight" onclick="releaseManualControl()" style="font-size:10px; padding:3px 8px;">
          ESC Release
        </button>
      </div>
    `;

    const contextMenuHtml = `
      <div id="mc-context-menu">
        <div class="ctx-header">
          <div class="ctx-title" id="ctx-menu-title">Item Inspector</div>
          <div class="ctx-sub" id="ctx-menu-sub">Coordinates (0, 0)</div>
        </div>
        <div id="ctx-menu-items"></div>
      </div>
    `;

    const container = document.createElement('div');
    container.id = 'mc-dynamic-modals';
    container.innerHTML = roomModalHtml + guideModalHtml + confirmModalHtml + manualOverlayHtml + contextMenuHtml;
    document.body.appendChild(container);

    makeDraggable(document.querySelector('#modal-room-switch .mc-modal-card'), document.querySelector('#modal-room-switch .draggable-handle'));
    makeDraggable(document.querySelector('#modal-confirm-warning .mc-modal-card'), document.querySelector('#modal-confirm-warning .draggable-handle'));
  }

  window.openRoomModal = function() {
    const el = document.getElementById('modal-room-switch');
    if (el) el.style.display = 'flex';
  };

  window.closeRoomModal = function() {
    const el = document.getElementById('modal-room-switch');
    if (el) el.style.display = 'none';
  };

  window.handleCaptchaClick = function() {
    const box = document.getElementById('captcha-check-box');
    const svg = document.getElementById('captcha-check-svg');
    const desc = document.getElementById('captcha-desc-text');

    window.isCaptchaVerified = true;
    if (window.humanCaptcha) window.humanCaptcha.isVerified = true;

    if (box) box.classList.add('verified');
    if (svg) svg.style.display = 'block';
    if (desc) {
      desc.textContent = 'Verified operator identity';
      desc.style.color = '#10b981';
    }
  };

  window.submitRoomSwitch = function() {
    const input = document.getElementById('input-room-id');
    const id = input ? input.value.trim() : '0123456789';
    if (!window.isCaptchaVerified && !(window.humanCaptcha && window.humanCaptcha.isVerified)) {
      handleCaptchaClick();
    }
    sessionStorage.setItem('amr_warehouse_verified', 'true');
    const ok = roomManager.switchRoom(id);
    if (ok) closeRoomModal();
  };

  window.loadTestRoom0123 = function() {
    const input = document.getElementById('input-room-id');
    if (input) input.value = '0123456789';
  };

  window.generateRandomRoomId = function() {
    let code = '';
    for (let i = 0; i < 10; i++) code += Math.floor(Math.random() * 10);
    const input = document.getElementById('input-room-id');
    if (input) input.value = code;
  };

  window.openGuideModal = function() {
    const el = document.getElementById('modal-guide-about');
    if (el) {
      renderComprehensiveGuideModal();
      el.style.display = 'flex';
    }
  };

  window.closeGuideModal = function() {
    const el = document.getElementById('modal-guide-about');
    if (el) {
      el.style.display = 'none';
      el.innerHTML = '';
    }
  };

  let pendingConfirmAction = null;

  window.confirmHaltAll = function() {
    pendingConfirmAction = () => {
      window.fleetHalted = true;
      if (window.AMR_FLEET) {
        window.AMR_FLEET.forEach(r => {
          r.currentSpeed = 0;
          if (r.state !== 'HALTED' && r.state !== 'IDLE_CHARGING') {
            r.previousState = r.state;
            r.state = 'HALTED';
          }
        });
      }
      if (typeof logTerminal === 'function') {
        logTerminal('SYSTEM', 'tag-traffic', "[HALT] EMERGENCY HALT ALL: All AMRs stopped immediately. Human workers remain active (ISO 3691-4).");
      }
      if (window.terminalBoss) {
        terminalBoss.printCli("EMERGENCY FLEET HALT TRIGGERED: All AMRs stopped. Human workers remain active.", "warn");
      }
    };
    const text = document.getElementById('confirm-modal-text');
    if (text) {
      text.innerHTML = `<strong>CRITICAL FLEET OVERRIDE:</strong><br>Are you sure you want to <strong>HALT ALL AMRs</strong> immediately?<br><span style="font-size:11px; color:#94a3b8;">Human workers will remain active in compliance with ISO 3691-4.</span>`;
    }
    const el = document.getElementById('modal-confirm-warning');
    if (el) el.style.display = 'flex';
  };

  window.confirmQuickReset = function(event) {
    if (event) event.stopPropagation();
    pendingConfirmAction = () => {
      window.fleetHalted = false;
      if (typeof logTerminal === 'function') {
        logTerminal('SYSTEM', 'tag-overtake', "Warehouse state, robot positions, and missions reset to defaults.");
      }
      if (typeof initAmrFleet === 'function') {
        initAmrFleet();
      } else if (window.AMR_FLEET) {
        window.AMR_FLEET.forEach((b, i) => {
          b.battery = 98;
          b.state = 'IDLE_CHARGING';
          b.carriedParcels = [];
          b.orderBox = null;
          b.x = b.homeX || b.x;
          b.y = b.homeY || b.y;
          b.gridX = Math.round(b.x);
          b.gridY = Math.round(b.y);
          b.path = [];
          b.pathIndex = 0;
          b.isWaiting = false;
        });
      }
      terminalBoss.clearConsole();
      terminalBoss.printCli("Warehouse state reset to default test configuration (0123456789).", "success");
    };
    const text = document.getElementById('confirm-modal-text');
    if (text) {
      text.innerHTML = `<strong>WAREHOUSE QUICK RESET:</strong><br>Reset all AMR trajectories, cargo payloads, and terminal stream to default test configuration (0123456789)?`;
    }
    const el = document.getElementById('modal-confirm-warning');
    if (el) el.style.display = 'flex';
  };

  window.closeConfirmModal = function() {
    const el = document.getElementById('modal-confirm-warning');
    if (el) el.style.display = 'none';
    pendingConfirmAction = null;
  };

  window.executeConfirmedAction = function() {
    if (pendingConfirmAction) pendingConfirmAction();
    closeConfirmModal();
  };

  // =========================================================================
  // 15. COMPREHENSIVE GUIDE & LEGEND MODAL (MOVED FROM BOTTOM BAR)
  // =========================================================================
  function renderComprehensiveGuideModal() {
    const modal = document.getElementById('modal-guide-about');
    if (!modal) return;

    modal.innerHTML = `
      <div class="mc-modal-card" style="width:620px; max-height:85vh; display:flex; flex-direction:column;">
        <div class="mc-modal-header draggable-handle">
          <strong style="color:#fff; font-size:13px; display:flex; align-items:center; gap:8px;">
            ${SVG.book} WAREHOUSE MISSION CONTROL GUIDE
          </strong>
          <button class="track-ctrl-close-btn" onclick="closeGuideModal()">&times;</button>
        </div>

        <div style="display:flex; border-bottom:1px solid rgba(255,255,255,0.1); background:#141822;">
          <button class="h-nav-tab active" id="tab-guide-btn" onclick="switchGuideTab('guide')" style="border-radius:0; border:none; padding:8px 14px;">Operational Guide</button>
          <button class="h-nav-tab" id="tab-legend-btn" onclick="switchGuideTab('legend')" style="border-radius:0; border:none; padding:8px 14px;">Legend &amp; Color Codes</button>
          <button class="h-nav-tab" id="tab-about-btn" onclick="switchGuideTab('about')" style="border-radius:0; border:none; padding:8px 14px;">Project &amp; Team Details</button>
        </div>

        <!-- TAB 1: OPERATIONAL GUIDE -->
        <div class="mc-modal-body" id="guide-tab-content" style="flex:1; overflow-y:auto;">
          <h4 style="color:#fff; margin-bottom:6px;">Decentralized AMR Fleet Coordination System</h4>
          <p style="font-size:11.5px; color:#cbd5e1; margin-bottom:10px; line-height:1.5;">
            Modern smart warehouses rely on fleets of Autonomous Mobile Robots (AMRs) operating without a central cloud bottleneck. In this digital twin, robots coordinate right-of-way, execute dynamic obstacle detours, and navigate high-density industrial storage aisles on a single unified floor.
          </p>
          <div style="background:#090c12; border:1px solid rgba(255,255,255,0.1); border-radius:6px; padding:10px; font-size:11px; line-height:1.6;">
            <strong style="color:#38bdf8;">Quick Operation Shortcuts:</strong><br>
            &bull; <strong>Camera:</strong> Free Orbit (Drag to rotate, Scroll to zoom), Follow AMR (locks behind robot), Top-Down view.<br>
            &bull; <strong>Right-Click Spawning:</strong> Right-click anywhere on the 3D or 2D floor to spawn AMRs, male/female workers, or pallet carts at that exact spot.<br>
            &bull; <strong>Manual Tele-Operation:</strong> Right-click an AMR or Worker and select <em>Take Control</em>. Walk directly into a robot's path to demonstrate LiDAR emergency safety stop and dynamic rerouting.<br>
            
            &bull; <strong>Terminal Boss:</strong> Type commands into Terminal 2 to inspect, modify, teleport, or dispatch robots.
          </div>
        </div>

        <!-- TAB 2: LEGEND & COLOR CODES (MOVED FROM BOTTOM BAR) -->
        <div class="mc-modal-body" id="legend-tab-content" style="flex:1; overflow-y:auto; display:none;">
          <div style="font-size:11px; color:#94a3b8; margin-bottom:8px;">
            Full color swatches and status designations for warehouse entities and AMR state machines:
          </div>
          <div class="legend-grid-modal">
            <div class="legend-card-item">
              <div class="legend-swatch" style="background:#151821; border:1px solid #282d37;"></div>
              <div><strong style="color:#fff;">3D Storage Rack</strong><br><span style="color:#94a3b8; font-size:9.5px;">5-Tier High-Density Pod</span></div>
            </div>
            <div class="legend-card-item">
              <div class="legend-swatch" style="background:#06b6d4;"></div>
              <div><strong style="color:#06b6d4;">Inbound Dock (P)</strong><br><span style="color:#94a3b8; font-size:9.5px;">Cyan: Idle / Yellow: Holding Load</span></div>
            </div>
            <div class="legend-card-item">
              <div class="legend-swatch" style="background:#f97316;"></div>
              <div><strong style="color:#f97316;">Outbound Bay (D)</strong><br><span style="color:#94a3b8; font-size:9.5px;">Orange: Idle / Yellow: Deposit Ready</span></div>
            </div>
            <div class="legend-card-item">
              <div class="legend-swatch" style="background:#22c55e; border:1px solid #86efac; box-shadow:0 0 6px rgba(34,197,94,0.6);"></div>
              <div><strong style="color:#22c55e;">Charging Station (C)</strong><br><span style="color:#94a3b8; font-size:9.5px;">48V LiFePO4 Fast Charger</span></div>
            </div>
            <div class="legend-card-item">
              <div class="legend-swatch" style="background:#1e293b; border:2px solid #38bdf8;"></div>
              <div><strong style="color:#fff;">Autonomous AMR</strong><br><span style="color:#94a3b8; font-size:9.5px;">Polar White Deck / Matte Chassis</span></div>
            </div>
            <div class="legend-card-item">
              <div class="legend-swatch" style="background:#0f172a; border:2px solid #38bdf8; box-shadow:0 0 6px #38bdf8;"></div>
              <div><strong style="color:#38bdf8;">Tracked AMR</strong><br><span style="color:#94a3b8; font-size:9.5px;">Active Camera Follow Target</span></div>
            </div>
            <div class="legend-card-item">
              <div class="legend-swatch" style="background:#b45309; border:1px solid #f59e0b;"></div>
              <div><strong style="color:#f59e0b;">Yielding / Waiting</strong><br><span style="color:#94a3b8; font-size:9.5px;">Right-of-Way Deceleration</span></div>
            </div>
            <div class="legend-card-item">
              <div class="legend-swatch" style="background:#0284c7; border:1px solid #38bdf8;"></div>
              <div><strong style="color:#38bdf8;">Overtaking Lane</strong><br><span style="color:#94a3b8; font-size:9.5px;">1.35x Bypass Cruise</span></div>
            </div>
            <div class="legend-card-item">
              <div class="legend-swatch" style="background:#7e22ce; border:1px solid #a855f7;"></div>
              <div><strong style="color:#c084fc;">Dynamic Reroute</strong><br><span style="color:#94a3b8; font-size:9.5px;">LiDAR Bottleneck Avoidance</span></div>
            </div>
            <div class="legend-card-item">
              <div class="legend-swatch" style="background:#111827; border:2px dashed #38bdf8;"></div>
              <div><strong style="color:#38bdf8;">Dotted Blue Rack</strong><br><span style="color:#94a3b8; font-size:9.5px;">Bot Placing Inbound Shipment</span></div>
            </div>
            <div class="legend-card-item">
              <div class="legend-swatch" style="background:#111827; border:2px dashed #ef4444;"></div>
              <div><strong style="color:#f87171;">Dotted Red Rack</strong><br><span style="color:#94a3b8; font-size:9.5px;">Bot Picking Outbound Order</span></div>
            </div>
            <div class="legend-card-item">
              <div class="legend-swatch" style="background:#b91c1c; border:1px solid #ef4444;"></div>
              <div><strong style="color:#f87171;">Low Battery Alert</strong><br><span style="color:#94a3b8; font-size:9.5px;">SoC &le; 25% (Autonomous Docking)</span></div>
            </div>
            <div class="legend-card-item">
              <div class="legend-swatch" style="background:#f97316;"></div>
              <div><strong style="color:#f97316;">Female Operator</strong><br><span style="color:#94a3b8; font-size:9.5px;">High-Vis Safety Orange Vest</span></div>
            </div>
            <div class="legend-card-item">
              <div class="legend-swatch" style="background:#10b981;"></div>
              <div><strong style="color:#10b981;">Male Operator</strong><br><span style="color:#94a3b8; font-size:9.5px;">Neon Emerald Green Vest</span></div>
            </div>
          </div>
        </div>

        <!-- TAB 3: PROJECT & TEAM DETAILS -->
        <div class="mc-modal-body" id="about-tab-content" style="flex:1; overflow-y:auto; display:none;">
          <div style="background:#090d14; border:1px solid rgba(56,189,248,0.3); border-radius:8px; padding:12px 14px; margin-bottom:12px;">
            <div style="font-size:11px; font-weight:800; color:#38bdf8; text-transform:uppercase; letter-spacing:1px; margin-bottom:4px;">
              SMART INDIA HACKATHON 2026
            </div>
            <div style="font-size:13px; font-weight:700; color:#ffffff; line-height:1.4; margin-bottom:10px;">
              Edge-AI Based Distributed Fleet Coordination for Autonomous Mobile Robots (AMRs) in Smart Warehouses
            </div>
            
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; font-size:11.5px; border-top:1px solid rgba(255,255,255,0.08); padding-top:10px;">
              <div><span style="color:#94a3b8;">Problem Statement ID:</span> <strong style="color:#fff;">26123</strong></div>
              <div><span style="color:#94a3b8;">Theme:</span> <strong style="color:#fff;">Smart Automation</strong></div>
              <div><span style="color:#94a3b8;">Category:</span> <strong style="color:#fff;">Software</strong></div>
              <div><span style="color:#94a3b8;">Organization:</span> <strong style="color:#fff;">Bharat Electronics Limited (BEL)</strong></div>
              <div><span style="color:#94a3b8;">Department:</span> <strong style="color:#fff;">Bharat Electronics Limited</strong></div>
              <div><span style="color:#94a3b8;">Team Name:</span> <strong style="color:#38bdf8;">Spirit_123</strong></div>
              <div><span style="color:#94a3b8;">Team ID:</span> <strong style="color:#38bdf8;">145299</strong></div>
              <div><span style="color:#94a3b8;">College:</span> <strong style="color:#fff;">SRM University-AP, Amaravati</strong></div>
            </div>
          </div>

          <div style="font-size:11.5px; font-weight:700; color:#fff; margin-bottom:8px; text-transform:uppercase; letter-spacing:0.5px;">
            TEAM MEMBERS:
          </div>
          <div style="display:grid; grid-template-columns:1fr 1fr; gap:8px; font-size:12px;">
            <div style="background:#090d14; border:1px solid rgba(255,255,255,0.1); border-radius:6px; padding:10px 12px; display:flex; align-items:center; gap:8px;">
              <span style="color:#38bdf8; font-weight:700; font-family:monospace;">1.</span>
              <strong style="color:#fff; font-size:12.5px;">Abhishek Paul Penumaka</strong>
            </div>
            <div style="background:#090d14; border:1px solid rgba(255,255,255,0.1); border-radius:6px; padding:10px 12px; display:flex; align-items:center; gap:8px;">
              <span style="color:#38bdf8; font-weight:700; font-family:monospace;">2.</span>
              <strong style="color:#fff; font-size:12.5px;">Yechuri Hitendra</strong>
            </div>
            <div style="background:#090d14; border:1px solid rgba(255,255,255,0.1); border-radius:6px; padding:10px 12px; display:flex; align-items:center; gap:8px;">
              <span style="color:#38bdf8; font-weight:700; font-family:monospace;">3.</span>
              <strong style="color:#fff; font-size:12.5px;">Venkata Nithien Kandula</strong>
            </div>
            <div style="background:#090d14; border:1px solid rgba(255,255,255,0.1); border-radius:6px; padding:10px 12px; display:flex; align-items:center; gap:8px;">
              <span style="color:#38bdf8; font-weight:700; font-family:monospace;">4.</span>
              <strong style="color:#fff; font-size:12.5px;">Jahnavi Sai Simhadri</strong>
            </div>
            <div style="background:#090d14; border:1px solid rgba(255,255,255,0.1); border-radius:6px; padding:10px 12px; display:flex; align-items:center; gap:8px;">
              <span style="color:#38bdf8; font-weight:700; font-family:monospace;">5.</span>
              <strong style="color:#fff; font-size:12.5px;">Kalari Vinay Chowdary</strong>
            </div>
            <div style="background:#090d14; border:1px solid rgba(255,255,255,0.1); border-radius:6px; padding:10px 12px; display:flex; align-items:center; gap:8px;">
              <span style="color:#38bdf8; font-weight:700; font-family:monospace;">6.</span>
              <strong style="color:#fff; font-size:12.5px;">Ediga Sai Vikas</strong>
            </div>
          </div>
        </div>

        <div class="mc-modal-footer">
          <button class="dropdown-trigger-btn highlight" onclick="closeGuideModal()">Close</button>
        </div>
      </div>
    `;

    makeDraggable(modal.querySelector('.mc-modal-card'), modal.querySelector('.draggable-handle'));
  }

  window.switchGuideTab = function(tab) {
    const guideBody = document.getElementById('guide-tab-content');
    const legendBody = document.getElementById('legend-tab-content');
    const aboutBody = document.getElementById('about-tab-content');

    const btnG = document.getElementById('tab-guide-btn');
    const btnL = document.getElementById('tab-legend-btn');
    const btnA = document.getElementById('tab-about-btn');

    if (guideBody) guideBody.style.display = tab === 'guide' ? 'block' : 'none';
    if (legendBody) legendBody.style.display = tab === 'legend' ? 'block' : 'none';
    if (aboutBody) aboutBody.style.display = tab === 'about' ? 'block' : 'none';

    if (btnG) btnG.classList.toggle('active', tab === 'guide');
    if (btnL) btnL.classList.toggle('active', tab === 'legend');
    if (btnA) btnA.classList.toggle('active', tab === 'about');
  };

  // =========================================================================
  // 16. MAIN TICK & ANIMATION INTEGRATION
  // =========================================================================
  let lastEnhanceTime = performance.now();

  function enhanceMainLoop() {
    const now = performance.now();
    const dt = Math.min(0.1, (now - lastEnhanceTime) / 1000);
    lastEnhanceTime = now;

    updateManualControl(dt);

    requestAnimationFrame(enhanceMainLoop);
  }

  // =========================================================================
  // 17. BOOT & DOM INJECTION
  // =========================================================================
  function bootMissionControl() {
    injectModernStyles();
    createUIModals();
    initManualControlListeners();
    initAccurateContextMenu();
    roomManager.init();
    terminalBoss.init();

    // Check if 1st visit needs warehouse access modal (Solid background, zero blur)
    if (!sessionStorage.getItem('amr_warehouse_verified')) {
      openRoomModal();
    }

    const check3DReady = setInterval(() => {
      if (window.scene3D) {
        clearInterval(check3DReady);
        setup3DMezzanineAndElevator();
        requestAnimationFrame(enhanceMainLoop);

        // Make floating HUD cards draggable
        const hudCard = document.getElementById('hud-card');
        if (hudCard) makeDraggable(hudCard, hudCard.querySelector('.hud-header'));

        const trackHud = document.querySelector('.bot-tracking-hud');
        if (trackHud) makeDraggable(trackHud, trackHud.querySelector('.tracking-hud-header'));

        const rackCard = document.getElementById('rack-inspector-card');
        if (rackCard) makeDraggable(rackCard, rackCard.querySelector('.rack-insp-header'));
      }
    }, 200);
  }

  // Inject styles immediately
  injectModernStyles();

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bootMissionControl);
  } else {
    bootMissionControl();
  }

})();
'''

with open('public/js/mission-control-enhancements.js', 'w', encoding='utf-8') as f:
    f.write(master_code)

print("Master mission-control-enhancements.js written successfully!")
