/**
 * ROOM MANAGER & MULTI-LEVEL WAREHOUSE LAYOUT
 * Supports 2-Level Mezzanine, Freight Elevators, Staircases, Diverse Human NPCs & AMRs.
 */

class RoomManager {
  constructor(planner) {
    this.planner = planner;
    this.currentRoomId = '0123456789';
    this.activeRoom = null;
    this.FIREBASE_URL = 'https://amr-fleet-26123-default-rtdb.firebaseio.com/rooms';
  }

  generateTestWarehouse() {
    return {
      id: '0123456789',
      name: 'BEL Multi-Level Smart Warehouse (2 Floors)',
      created: Date.now(),
      lastUpdated: Date.now(),
      gridSize: { width: 80, height: 50 },
      // 2 Floors Definition
      levels: [
        { level: 1, name: 'Ground Floor (Primary Logistics)', elevation: 0 },
        { level: 2, name: 'Mezzanine Level (High-Density Staging)', elevation: 4.2 }
      ],
      // 2 Industrial Staircases
      stairs: [
        { id: 'stair_1', x: 38, y: 12, width: 4, height: 2, label: 'Mezzanine Stair North' },
        { id: 'stair_2', x: 38, y: 36, width: 4, height: 2, label: 'Mezzanine Stair South' }
      ],
      // Industrial Freight Elevator (Connecting Floor 1 and Floor 2)
      elevators: [
        { id: 'ELEV-01', x: 40, y: 25, approachX: 42, approachY: 25, currentFloor: 1, targetFloor: 1, isMoving: false }
      ],
      // Fast Charging Bays
      chargers: [
        { id: 'CH-01', x: 2, y: 2, approachX: 3, approachY: 2, floor: 1 },
        { id: 'CH-02', x: 5, y: 2, approachX: 6, approachY: 2, floor: 1 },
        { id: 'CH-03', x: 8, y: 2, approachX: 9, approachY: 2, floor: 1 },
        { id: 'CH-04', x: 11, y: 2, approachX: 12, approachY: 2, floor: 1 },
        { id: 'CH-05', x: 2, y: 47, approachX: 3, approachY: 47, floor: 1 },
        { id: 'CH-06', x: 5, y: 47, approachX: 6, approachY: 47, floor: 1 },
        { id: 'CH-07', x: 8, y: 47, approachX: 9, approachY: 47, floor: 1 },
        { id: 'CH-08', x: 11, y: 47, approachX: 12, approachY: 47, floor: 1 }
      ],
      // Inbound & Outbound Docks
      stations: [
        { id: 'IN-01', type: 'inbound', x: 1, y: 10, approachX: 2, approachY: 10, label: 'Inbound Dock 1', floor: 1 },
        { id: 'IN-02', type: 'inbound', x: 1, y: 20, approachX: 2, approachY: 20, label: 'Inbound Dock 2', floor: 1 },
        { id: 'IN-03', type: 'inbound', x: 1, y: 30, approachX: 2, approachY: 30, label: 'Inbound Dock 3', floor: 1 },
        { id: 'OUT-01', type: 'outbound', x: 78, y: 10, approachX: 77, approachY: 10, label: 'Outbound Bay 1', floor: 1 },
        { id: 'OUT-02', type: 'outbound', x: 78, y: 20, approachX: 77, approachY: 20, label: 'Outbound Bay 2', floor: 1 },
        { id: 'OUT-03', type: 'outbound', x: 78, y: 30, approachX: 77, approachY: 30, label: 'Outbound Bay 3', floor: 1 }
      ],
      // Storage Racks across both floors
      racks: this._generateRacksGrid(80, 50),
      // 8 Autonomous Mobile Robots
      robots: [
        { id: 'AMR-01', x: 3, y: 2, floor: 1, heading: 0, battery: 96, state: 'IDLE', speed: 1.2, task: 'Shelving PKG-1673', powerDraw: 474 },
        { id: 'AMR-02', x: 6, y: 2, floor: 1, heading: 0, battery: 92, state: 'IDLE', speed: 1.2, task: 'Awaiting Wave', powerDraw: 280 },
        { id: 'AMR-03', x: 9, y: 2, floor: 1, heading: 0, battery: 88, state: 'IDLE', speed: 1.2, task: 'Inbound Transit', powerDraw: 410 },
        { id: 'AMR-04', x: 12, y: 2, floor: 1, heading: 0, battery: 95, state: 'IDLE', speed: 1.2, task: 'Highway Transit', powerDraw: 390 },
        { id: 'AMR-05', x: 42, y: 25, floor: 2, heading: Math.PI, battery: 84, state: 'IDLE', speed: 1.2, task: 'Floor 2 Staging', powerDraw: 430 },
        { id: 'AMR-06', x: 6, y: 47, floor: 1, heading: 0, battery: 85, state: 'IDLE', speed: 1.2, task: 'Dock Approach', powerDraw: 350 },
        { id: 'AMR-07', x: 9, y: 47, floor: 1, heading: 0, battery: 91, state: 'IDLE', speed: 1.2, task: 'Awaiting Order', powerDraw: 290 },
        { id: 'AMR-08', x: 12, y: 47, floor: 1, heading: 0, battery: 89, state: 'IDLE', speed: 1.2, task: 'Charging Standby', powerDraw: 260 }
      ],
      // Male and Female Human Workers in Diverse Attire
      humans: [
        { id: 'Worker-1', name: 'Rajesh K.', gender: 'male', vestColor: 0xffb300, pantsColor: 0x1e293b, x: 22, y: 24, floor: 1, heading: 0, path: [{x:22,y:24},{x:22,y:32},{x:28,y:32},{x:28,y:24}] },
        { id: 'Worker-2', name: 'Jahnavi S.', gender: 'female', vestColor: 0x10b981, pantsColor: 0x334155, x: 50, y: 16, floor: 1, heading: 0, path: [{x:50,y:16},{x:50,y:24},{x:56,y:24},{x:56,y:16}] },
        { id: 'Worker-3', name: 'Hitendra Y.', gender: 'male', vestColor: 0xef4444, pantsColor: 0x0f172a, x: 65, y: 34, floor: 1, heading: 0, path: [{x:65,y:34},{x:72,y:34},{x:72,y:42},{x:65,y:42}] },
        { id: 'Worker-4', name: 'Sarah M.', gender: 'female', vestColor: 0xf59e0b, pantsColor: 0x1e3a8a, x: 44, y: 20, floor: 2, heading: 0, path: [{x:44,y:20},{x:44,y:28},{x:48,y:28},{x:48,y:20}] }
      ],
      inventory: {
        totalCartons: 1512,
        inboundCompleted: 86,
        outboundCompleted: 74,
        activeOrders: 14
      }
    };
  }

  _generateRacksGrid(width, height) {
    const racks = [];
    let rackCounter = 1;
    const blockXStarts = [16, 26, 46, 56, 66];
    const blockYStarts = [6, 16, 26, 36];

    for (const bx of blockXStarts) {
      for (const by of blockYStarts) {
        for (let dy = 0; dy < 6; dy++) {
          const rackId1 = `R-${String(rackCounter++).padStart(4, '0')}`;
          const rackId2 = `R-${String(rackCounter++).padStart(4, '0')}`;
          racks.push({
            id: rackId1,
            x: bx,
            y: by + dy,
            tierCount: 5,
            floor: (bx >= 46 && by <= 26) ? 2 : 1, // Some on Mezzanine level!
            bufferFace: { x: bx - 1, y: by + dy },
            waitingSpot: { x: bx - 2, y: by + dy }
          });
          racks.push({
            id: rackId2,
            x: bx + 1,
            y: by + dy,
            tierCount: 5,
            floor: (bx >= 46 && by <= 26) ? 2 : 1,
            bufferFace: { x: bx + 2, y: by + dy },
            waitingSpot: { x: bx + 3, y: by + dy }
          });
        }
      }
    }
    return racks;
  }

  async loadRoom(roomId) {
    this.currentRoomId = roomId;
    let roomData = null;

    const cached = localStorage.getItem(`amr_room_${roomId}`);
    if (cached) {
      try { roomData = JSON.parse(cached); } catch (e) {}
    }

    if (!roomData && roomId === '0123456789') {
      roomData = this.generateTestWarehouse();
    } else if (!roomData) {
      roomData = this.generateTestWarehouse();
      roomData.id = roomId;
      roomData.name = `Warehouse Unit ${roomId}`;
    }

    this.applyOfflineCatchup(roomData);
    this.activeRoom = roomData;
    this.saveRoom(roomData);
    this.applyToPlanner(roomData);

    return roomData;
  }

  resetTestRoom() {
    const testData = this.generateTestWarehouse();
    this.activeRoom = testData;
    this.saveRoom(testData);
    this.applyToPlanner(testData);
    return testData;
  }

  applyOfflineCatchup(room) {
    if (!room.lastUpdated) {
      room.lastUpdated = Date.now();
      return;
    }
    const now = Date.now();
    const elapsedSeconds = Math.max(0, Math.min(86400, (now - room.lastUpdated) / 1000));
    if (elapsedSeconds < 2) return;

    const ordersProcessed = Math.floor(elapsedSeconds / 30);
    room.inventory.inboundCompleted += Math.floor(ordersProcessed * 0.5);
    room.inventory.outboundCompleted += Math.floor(ordersProcessed * 0.5);

    room.robots.forEach(bot => {
      if (bot.x <= 15 && (bot.y <= 3 || bot.y >= 46)) {
        bot.battery = Math.min(100, Math.round(bot.battery + elapsedSeconds * 0.2));
      } else {
        bot.battery = Math.max(15, Math.round(bot.battery - elapsedSeconds * 0.04));
      }
    });

    room.lastUpdated = now;
  }

  saveRoom(room) {
    room.lastUpdated = Date.now();
    try {
      localStorage.setItem(`amr_room_${room.id}`, JSON.stringify(room));
    } catch (e) {}
    try {
      fetch(`${this.FIREBASE_URL}/${room.id}.json`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(room)
      }).catch(() => {});
    } catch (e) {}
  }

  applyToPlanner(room) {
    if (!this.planner) return;
    const { width, height } = room.gridSize;

    for (let x = 0; x < width; x++) {
      for (let y = 0; y < height; y++) {
        this.planner.grid[x][y] = CELL_TYPE.HIGHWAY;
      }
    }
    this.planner.cellLabels.clear();

    room.racks.forEach(rack => {
      this.planner.classifyCell(rack.x, rack.y, CELL_TYPE.RACK, rack.id);
      if (rack.bufferFace) {
        this.planner.classifyCell(rack.bufferFace.x, rack.bufferFace.y, CELL_TYPE.BUFFER, rack.id, rack.waitingSpot);
      }
    });

    room.chargers.forEach(ch => {
      this.planner.classifyCell(ch.x, ch.y, CELL_TYPE.OBSTACLE, ch.id);
      this.planner.classifyCell(ch.approachX, ch.approachY, CELL_TYPE.TERMINAL_BUFFER, ch.id);
    });

    room.stations.forEach(st => {
      this.planner.classifyCell(st.x, st.y, CELL_TYPE.OBSTACLE, st.id);
      this.planner.classifyCell(st.approachX, st.approachY, CELL_TYPE.TERMINAL_BUFFER, st.id);
    });

    // Elevators
    (room.elevators || []).forEach(elv => {
      this.planner.classifyCell(elv.x, elv.y, CELL_TYPE.OBSTACLE, elv.id);
      this.planner.classifyCell(elv.approachX, elv.approachY, CELL_TYPE.TERMINAL_BUFFER, elv.id);
    });

    // Stairs
    (room.stairs || []).forEach(st => {
      for (let dx = 0; dx < st.width; dx++) {
        for (let dy = 0; dy < st.height; dy++) {
          this.planner.classifyCell(st.x + dx, st.y + dy, CELL_TYPE.OBSTACLE, st.id);
        }
      }
    });
  }
}
