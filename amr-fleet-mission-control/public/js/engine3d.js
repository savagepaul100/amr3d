/**
 * EDGE-AI 3D WAREHOUSE DIGITAL TWIN ENGINE (THREE.JS)
 * 
 * Features:
 * - Vikas's authentic Real AMR 3D models with rotating LiDAR & perimeter LED halos.
 * - 2-Level Mezzanine Catwalks + Working Industrial Freight Elevator.
 * - 2 Steel Staircases with Safety Handrails.
 * - Male and Female Human Workers in Diverse Industrial Attire.
 * - C-V2X 5.9 GHz Peer-to-Peer V2V Communication Mesh Lines.
 * - Elegant Black & White Theme (Obsidian floor, Polar White decks, High-Contrast Racks).
 * - Full Camera Presets: Orbit, Follow AMR, Isometric, Top-Down.
 */

class WarehouseEngine3D {
  constructor(containerId, planner) {
    this.container = document.getElementById(containerId);
    this.planner = planner;

    this.gridWidth = 80;
    this.gridHeight = 50;
    this.C_SIZE = 1.6; // Cell size in 3D world units
    this.HALF_W = 40;
    this.HALF_H = 25;

    // Three.js Core
    this.scene = null;
    this.camera = null;
    this.renderer = null;
    this.controls = null;
    this.clock = new THREE.Clock();

    // Visual Flags
    this.showLidar = true;
    this.showPaths = true;
    this.showWire = false;
    this.showV2V = true;
    this.showWorkers = true;

    // Simulation State
    this.simSpeed = 1;
    this.isAutomationPaused = false;
    this.spectatingBotId = null;

    // Entities
    this.robots = [];
    this.humans = [];
    this.elevators = [];
    this.stairs = [];
    this.racks = [];

    // Mesh Groups
    this.robotMeshes = new Map();
    this.humanMeshes = new Map();
    this.v2vMeshGroup = new THREE.Group();
    this.elevatorMeshGroup = new THREE.Group();
    this.pathLinesGroup = new THREE.Group();

    this.initScene();
    this.initLights();
    this.animate();
  }

  gridTo3D(gx, gy, elevation = 0) {
    return {
      x: (gx - this.HALF_W + 0.5) * this.C_SIZE,
      y: elevation,
      z: (gy - this.HALF_H + 0.5) * this.C_SIZE
    };
  }

  initScene() {
    if (!this.container) return;
    const width = this.container.clientWidth || window.innerWidth;
    const height = this.container.clientHeight || (window.innerHeight - 80);

    this.scene = new THREE.Scene();
    this.scene.background = new THREE.Color(0x0a0c10); // Deep Carbon Slate
    this.scene.fog = new THREE.FogExp2(0x0a0c10, 0.006);

    // Camera
    this.camera = new THREE.PerspectiveCamera(45, width / height, 0.5, 2000);
    this.camera.position.set(0, 58, 68);

    // Renderer
    this.renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: 'high-performance' });
    this.renderer.setSize(width, height);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    this.renderer.toneMapping = THREE.ACESFilmicToneMapping;
    this.renderer.toneMappingExposure = 1.25;
    this.renderer.shadowMap.enabled = true;
    this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    this.container.innerHTML = '';
    this.container.appendChild(this.renderer.domElement);

    // Orbit Controls
    this.controls = new THREE.OrbitControls(this.camera, this.renderer.domElement);
    this.controls.enableDamping = true;
    this.controls.dampingFactor = 0.08;
    this.controls.maxPolarAngle = Math.PI / 2 - 0.02;
    this.controls.minDistance = 6;
    this.controls.maxDistance = 350;
    this.controls.target.set(0, 0, 0);

    // Resize Handler
    window.addEventListener('resize', () => {
      if (!this.container) return;
      const w = this.container.clientWidth;
      const h = this.container.clientHeight;
      this.camera.aspect = w / h;
      this.camera.updateProjectionMatrix();
      this.renderer.setSize(w, h);
    });

    this.scene.add(this.v2vMeshGroup);
    this.scene.add(this.elevatorMeshGroup);
    this.scene.add(this.pathLinesGroup);

    this.buildWarehouseFloors();
  }

  initLights() {
    const hemiLight = new THREE.HemisphereLight(0xffffff, 0x1e2430, 1.4);
    this.scene.add(hemiLight);

    const mainSpot = new THREE.DirectionalLight(0xffffff, 2.2);
    mainSpot.position.set(30, 90, 45);
    mainSpot.castShadow = true;
    mainSpot.shadow.mapSize.width = 2048;
    mainSpot.shadow.mapSize.height = 2048;
    this.scene.add(mainSpot);

    const rimLight = new THREE.DirectionalLight(0xcfd8dc, 1.2);
    rimLight.position.set(-45, 65, -45);
    this.scene.add(rimLight);
  }

  buildWarehouseFloors() {
    const totalW = this.gridWidth * this.C_SIZE;
    const totalH = this.gridHeight * this.C_SIZE;

    // 1. Level 1: Ground Floor Concrete Slab
    const floorGeo = new THREE.PlaneGeometry(totalW, totalH);
    const floorMat = new THREE.MeshStandardMaterial({
      color: 0x0f131a,
      roughness: 0.65,
      metalness: 0.2
    });
    const groundFloor = new THREE.Mesh(floorGeo, floorMat);
    groundFloor.rotation.x = -Math.PI / 2;
    groundFloor.position.set(0, 0, 0);
    groundFloor.receiveShadow = true;
    this.scene.add(groundFloor);

    // Crisp Floor Grid
    const grid = new THREE.GridHelper(Math.max(totalW, totalH), Math.max(this.gridWidth, this.gridHeight), 0x272e3d, 0x141a24);
    grid.position.set(0, 0.02, 0);
    this.scene.add(grid);

    // Highway White Safety Markings
    const lineMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
    const createStripe = (x, z, sx, sz) => {
      const geo = new THREE.PlaneGeometry(sx, sz);
      const mesh = new THREE.Mesh(geo, lineMat);
      mesh.rotation.x = -Math.PI / 2;
      mesh.position.set(x, 0.03, z);
      this.scene.add(mesh);
    };
    createStripe(0, -6, totalW * 0.92, 0.12);
    createStripe(0, 6, totalW * 0.92, 0.12);

    // 2. Level 2: Mezzanine Catwalk Elevated Deck (Elevation y = 4.2m)
    // Covers the East half of the warehouse (x > 0)
    const mezzW = totalW * 0.45;
    const mezzH = totalH * 0.75;
    const mezzGeo = new THREE.BoxGeometry(mezzW, 0.25, mezzH);
    const mezzMat = new THREE.MeshStandardMaterial({
      color: 0x1e2430,
      metalness: 0.8,
      roughness: 0.3
    });
    const mezzanine = new THREE.Mesh(mezzGeo, mezzMat);
    mezzanine.position.set(mezzW * 0.52, 4.2, 0);
    mezzanine.receiveShadow = true;
    this.scene.add(mezzanine);

    // Safety Yellow Railings around Mezzanine
    const railMat = new THREE.MeshStandardMaterial({ color: 0xf59e0b, roughness: 0.3 });
    const railGeo = new THREE.CylinderGeometry(0.04, 0.04, mezzH);
    const westRail = new THREE.Mesh(railGeo, railMat);
    westRail.rotation.x = Math.PI / 2;
    westRail.position.set(mezzW * 0.52 - mezzW / 2, 4.2 + 0.9, 0);
    this.scene.add(westRail);

    // Support Columns under Mezzanine
    const colGeo = new THREE.CylinderGeometry(0.35, 0.35, 4.2, 16);
    const colMat = new THREE.MeshStandardMaterial({ color: 0x111622, metalness: 0.8 });
    for (let cx = 5; cx < mezzW; cx += 14) {
      for (let cz = -mezzH / 2 + 5; cz < mezzH / 2; cz += 14) {
        const col = new THREE.Mesh(colGeo, colMat);
        col.position.set(mezzW * 0.52 - mezzW / 2 + cx, 2.1, cz);
        this.scene.add(col);
      }
    }
  }

  loadRoomData(room) {
    this.clearSceneEntities();

    this.gridWidth = room.gridSize.width;
    this.gridHeight = room.gridSize.height;

    this.buildRacks(room.racks || []);
    this.buildChargers(room.chargers || []);
    this.buildStations(room.stations || []);
    this.buildStairs(room.stairs || []);
    this.buildElevators(room.elevators || []);

    // AMRs
    this.robots = (room.robots || []).map((b, idx) => ({
      ...b,
      currentSpeed: 0,
      heading: b.heading || 0,
      ledStatus: 'GREEN',
      lidarAngle: 0,
      state: b.state || 'IDLE',
      subState: 'HIGHWAY',
      targetRack: null,
      path: [],
      pathIndex: 0,
      manualOverride: false,
      elevation: b.floor === 2 ? 4.2 : 0
    }));

    this.robots.forEach((b, idx) => this.createRobotMesh(b, idx + 1));

    // Humans
    this.humans = (room.humans || []).map(h => ({
      ...h,
      currentSpeed: 0.9,
      pathIndex: 0,
      walkPhase: 0,
      manualOverride: false,
      elevation: h.floor === 2 ? 4.2 : 0
    }));

    this.humans.forEach(h => this.createHumanMesh(h));
  }

  clearSceneEntities() {
    this.robotMeshes.forEach(mesh => this.scene.remove(mesh));
    this.robotMeshes.clear();
    this.humanMeshes.forEach(mesh => this.scene.remove(mesh));
    this.humanMeshes.clear();
    this.elevatorMeshGroup.clear();
    this.pathLinesGroup.clear();

    if (this.racksMesh) {
      this.scene.remove(this.racksMesh);
      this.racksMesh = null;
    }
    if (this.stairsGroup) {
      this.scene.remove(this.stairsGroup);
      this.stairsGroup = null;
    }
  }

  /**
   * Vikas's Authentic Real AMR 3D Model Constructor
   */
  createRobotMesh(bot, num) {
    const root = new THREE.Group();
    root.name = bot.id;

    // A. Lower Chassis (Matte obsidian black base with safety bumpers)
    const chassisGeo = new THREE.BoxGeometry(1.24, 0.28, 0.96);
    const chassisMat = new THREE.MeshStandardMaterial({ color: 0x141720, roughness: 0.5, metalness: 0.4 });
    const chassis = new THREE.Mesh(chassisGeo, chassisMat);
    chassis.position.y = 0.20;
    root.add(chassis);

    // Front & rear safety bumpers
    const bumperGeo = new THREE.BoxGeometry(0.12, 0.20, 0.98);
    const bumperMat = new THREE.MeshStandardMaterial({ color: 0x050608, roughness: 0.9 });
    const frontBumper = new THREE.Mesh(bumperGeo, bumperMat);
    frontBumper.position.set(0.65, 0.20, 0);
    root.add(frontBumper);

    const rearBumper = new THREE.Mesh(bumperGeo, bumperMat);
    rearBumper.position.set(-0.65, 0.20, 0);
    root.add(rearBumper);

    // B. Upper Housing (Stark Polar White with black tech seam)
    const shellGeo = new THREE.BoxGeometry(1.14, 0.18, 0.88);
    const shellMat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.2, metalness: 0.1 });
    const shell = new THREE.Mesh(shellGeo, shellMat);
    shell.position.y = 0.38;
    root.add(shell);

    // Center tech groove
    const groove = new THREE.Mesh(
      new THREE.BoxGeometry(1.16, 0.03, 0.26),
      new THREE.MeshStandardMaterial({ color: 0x0a0c10, roughness: 0.8 })
    );
    groove.position.y = 0.46;
    root.add(groove);

    // C. Drive Wheels (Rubber treads + bright silver center rims)
    const wheelGeo = new THREE.CylinderGeometry(0.18, 0.18, 0.08, 24);
    wheelGeo.rotateZ(Math.PI / 2);
    const tireMat = new THREE.MeshStandardMaterial({ color: 0x090b0e, roughness: 0.95 });
    const rimGeo = new THREE.CylinderGeometry(0.10, 0.10, 0.085, 16);
    rimGeo.rotateZ(Math.PI / 2);
    const rimMat = new THREE.MeshStandardMaterial({ color: 0xe2e8f0, metalness: 0.8, roughness: 0.2 });

    const leftWheel = new THREE.Group();
    leftWheel.add(new THREE.Mesh(wheelGeo, tireMat));
    leftWheel.add(new THREE.Mesh(rimGeo, rimMat));
    leftWheel.position.set(0, 0.18, 0.48);
    root.add(leftWheel);

    const rightWheel = new THREE.Group();
    rightWheel.add(new THREE.Mesh(wheelGeo, tireMat));
    rightWheel.add(new THREE.Mesh(rimGeo, rimMat));
    rightWheel.position.set(0, 0.18, -0.48);
    root.add(rightWheel);

    // D. Elevating Turntable Deck
    const turntableGeo = new THREE.CylinderGeometry(0.38, 0.38, 0.04, 32);
    const turntableMat = new THREE.MeshStandardMaterial({ color: 0x272a33, metalness: 0.65, roughness: 0.35 });
    const turntable = new THREE.Mesh(turntableGeo, turntableMat);
    turntable.position.y = 0.44;
    root.add(turntable);

    // E. 360° Safety LiDAR Sensor Puck
    const lidarDome = new THREE.Mesh(
      new THREE.CylinderGeometry(0.06, 0.06, 0.08, 16),
      new THREE.MeshStandardMaterial({ color: 0x000000, roughness: 0.1, metalness: 0.9 })
    );
    lidarDome.position.set(0.44, 0.50, 0.28);
    root.add(lidarDome);
    root.lidarRef = lidarDome;

    // Forward Safety LiDAR Laser Beam Fan
    const laserGeo = new THREE.ConeGeometry(1.6, 1.3, 16, 1, true, -Math.PI / 4, Math.PI / 2);
    laserGeo.rotateZ(Math.PI / 2);
    laserGeo.rotateY(-Math.PI / 2);
    const laserMat = new THREE.MeshBasicMaterial({ color: 0x00e5ff, transparent: true, opacity: 0.14, side: THREE.DoubleSide });
    const laserFan = new THREE.Mesh(laserGeo, laserMat);
    laserFan.position.set(0.50, 0.50, 0);
    laserFan.visible = this.showLidar;
    root.add(laserFan);
    root.laserRef = laserFan;

    // F. Perimeter Status LED Halo
    const haloGeo = new THREE.BoxGeometry(1.26, 0.035, 0.98);
    const haloMat = new THREE.MeshBasicMaterial({ color: 0x10b981, transparent: true, opacity: 0.95 });
    const statusHalo = new THREE.Mesh(haloGeo, haloMat);
    statusHalo.position.y = 0.29;
    root.add(statusHalo);
    root.haloRef = statusHalo;

    // Dual front headlights
    const hlMat = new THREE.MeshBasicMaterial({ color: 0xffffff });
    const hlL = new THREE.Mesh(new THREE.BoxGeometry(0.03, 0.05, 0.08), hlMat);
    hlL.position.set(0.63, 0.29, 0.28);
    root.add(hlL);
    const hlR = new THREE.Mesh(new THREE.BoxGeometry(0.03, 0.05, 0.08), hlMat);
    hlR.position.set(0.63, 0.29, -0.28);
    root.add(hlR);

    // Initial 3D Position
    const pos = this.gridTo3D(bot.x, bot.y, bot.elevation || 0);
    root.position.set(pos.x, pos.y, pos.z);

    this.scene.add(root);
    this.robotMeshes.set(bot.id, root);
  }

  /**
   * Male and Female Human Workers in Diverse Attire
   */
  createHumanMesh(human) {
    const root = new THREE.Group();
    root.name = human.id;

    // Pants / Legs
    const pantsMat = new THREE.MeshStandardMaterial({ color: human.pantsColor || 0x1e293b, roughness: 0.8 });
    const legGeo = new THREE.BoxGeometry(0.18, 0.75, 0.18);
    const lLeg = new THREE.Mesh(legGeo, pantsMat);
    lLeg.position.set(-0.11, 0.38, 0);
    root.add(lLeg);
    root.lLeg = lLeg;

    const rLeg = new THREE.Mesh(legGeo, pantsMat);
    rLeg.position.set(0.11, 0.38, 0);
    root.add(rLeg);
    root.rLeg = rLeg;

    // Torso with High-Vis Safety Vest
    const vestMat = new THREE.MeshStandardMaterial({ color: human.vestColor || 0xffb300, roughness: 0.4 });
    const torsoGeo = new THREE.BoxGeometry(human.gender === 'female' ? 0.38 : 0.44, 0.60, 0.25);
    const torso = new THREE.Mesh(torsoGeo, vestMat);
    torso.position.y = 1.05;
    root.add(torso);

    // Head
    const headMat = new THREE.MeshStandardMaterial({ color: 0xf5d0b0 });
    const head = new THREE.Mesh(new THREE.SphereGeometry(0.13, 12, 12), headMat);
    head.position.y = 1.48;
    root.add(head);

    // Hair or Hardhat
    const hatMat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.3 }); // White Supervisor Hardhat
    const hat = new THREE.Mesh(new THREE.CylinderGeometry(0.17, 0.21, 0.10, 12), hatMat);
    hat.position.y = 1.58;
    root.add(hat);

    // Female Hair Knot if female
    if (human.gender === 'female') {
      const hairMat = new THREE.MeshStandardMaterial({ color: 0x271e1b, roughness: 0.9 });
      const hairBun = new THREE.Mesh(new THREE.SphereGeometry(0.07, 8, 8), hairMat);
      hairBun.position.set(0, 1.48, -0.14);
      root.add(hairBun);
    }

    const pos = this.gridTo3D(human.x, human.y, human.elevation || 0);
    root.position.set(pos.x, pos.y, pos.z);

    this.scene.add(root);
    this.humanMeshes.set(human.id, root);
  }

  buildRacks(racks) {
    if (!racks || racks.length === 0) return;
    const count = racks.length;

    // High-Contrast Monochrome High-Bay Racks
    const rackGeo = new THREE.BoxGeometry(this.C_SIZE * 0.88, 3.2, this.C_SIZE * 0.88);
    const rackMat = new THREE.MeshStandardMaterial({ color: 0x161b24, roughness: 0.4, metalness: 0.6 });
    this.racksMesh = new THREE.InstancedMesh(rackGeo, rackMat, count);
    this.racksMesh.castShadow = true;
    this.racksMesh.receiveShadow = true;

    const dummy = new THREE.Object3D();
    racks.forEach((rack, i) => {
      const elev = rack.floor === 2 ? 4.2 : 0;
      const pos = this.gridTo3D(rack.x, rack.y, elev);
      dummy.position.set(pos.x, pos.y + 1.6, pos.z);
      dummy.updateMatrix();
      this.racksMesh.setMatrixAt(i, dummy.matrix);
    });
    this.racksMesh.instanceMatrix.needsUpdate = true;
    this.scene.add(this.racksMesh);
  }

  buildElevators(elevators) {
    elevators.forEach(elv => {
      const elvGroup = new THREE.Group();
      elvGroup.name = elv.id;

      // Shaft Frame Columns (Connecting Ground Floor to Mezzanine)
      const shaftGeo = new THREE.BoxGeometry(this.C_SIZE * 1.2, 5.2, this.C_SIZE * 1.2);
      const shaftEdges = new THREE.EdgesGeometry(shaftGeo);
      const shaftLines = new THREE.LineSegments(shaftEdges, new THREE.LineBasicMaterial({ color: 0xffffff, linewidth: 2 }));
      shaftLines.position.y = 2.6;
      elvGroup.add(shaftLines);

      // Elevator Carriage Lift Platform
      const cabGeo = new THREE.BoxGeometry(this.C_SIZE * 1.1, 0.15, this.C_SIZE * 1.1);
      const cabMat = new THREE.MeshStandardMaterial({ color: 0xf59e0b, metalness: 0.8 });
      const cab = new THREE.Mesh(cabGeo, cabMat);
      cab.position.y = 0.1;
      cab.name = 'carriage';
      elvGroup.add(cab);
      elv.cabRef = cab;

      const pos = this.gridTo3D(elv.x, elv.y, 0);
      elvGroup.position.set(pos.x, 0, pos.z);
      this.elevatorMeshGroup.add(elvGroup);
    });
  }

  buildStairs(stairs) {
    this.stairsGroup = new THREE.Group();
    const stairMat = new THREE.MeshStandardMaterial({ color: 0x272e3d, metalness: 0.85, roughness: 0.3 });
    const railingMat = new THREE.MeshStandardMaterial({ color: 0xf59e0b, roughness: 0.4 });

    stairs.forEach(st => {
      const stairObj = new THREE.Group();
      const steps = 12;
      const stepWidth = st.width * this.C_SIZE * 0.45;
      const stepRise = 4.2 / steps;
      const stepRun = (st.height * this.C_SIZE) / steps;

      for (let s = 0; s < steps; s++) {
        const stepGeo = new THREE.BoxGeometry(stepWidth, 0.08, stepRun);
        const stepMesh = new THREE.Mesh(stepGeo, stairMat);
        stepMesh.position.set(0, (s + 1) * stepRise, s * stepRun);
        stairObj.add(stepMesh);
      }

      // Handrail
      const railGeo = new THREE.CylinderGeometry(0.04, 0.04, steps * stepRun * 1.2);
      const rail = new THREE.Mesh(railGeo, railingMat);
      rail.rotation.x = Math.PI / 4;
      rail.position.set(stepWidth / 2 + 0.05, 2.1 + 0.8, (steps * stepRun) / 2);
      stairObj.add(rail);

      const pos = this.gridTo3D(st.x, st.y, 0);
      stairObj.position.set(pos.x, 0, pos.z);
      this.stairsGroup.add(stairObj);
    });

    this.scene.add(this.stairsGroup);
  }

  buildChargers(chargers) {
    const padGeo = new THREE.BoxGeometry(this.C_SIZE * 0.85, 0.06, this.C_SIZE * 0.85);
    const padMat = new THREE.MeshStandardMaterial({ color: 0x10b981, roughness: 0.4 });
    const padMesh = new THREE.InstancedMesh(padGeo, padMat, chargers.length);

    const dummy = new THREE.Object3D();
    chargers.forEach((ch, i) => {
      const pos = this.gridTo3D(ch.x, ch.y, ch.floor === 2 ? 4.2 : 0);
      dummy.position.set(pos.x, pos.y + 0.03, pos.z);
      dummy.updateMatrix();
      padMesh.setMatrixAt(i, dummy.matrix);
    });
    padMesh.instanceMatrix.needsUpdate = true;
    this.scene.add(padMesh);
  }

  buildStations(stations) {
    const stationGeo = new THREE.BoxGeometry(this.C_SIZE * 0.9, 0.35, this.C_SIZE * 0.9);
    const inMat = new THREE.MeshStandardMaterial({ color: 0x0284c7 });
    const outMat = new THREE.MeshStandardMaterial({ color: 0xd97706 });

    stations.forEach(st => {
      const mat = st.type === 'inbound' ? inMat : outMat;
      const mesh = new THREE.Mesh(stationGeo, mat);
      const pos = this.gridTo3D(st.x, st.y, st.floor === 2 ? 4.2 : 0);
      mesh.position.set(pos.x, pos.y + 0.18, pos.z);
      this.scene.add(mesh);
    });
  }

  /**
   * 60 FPS Render Loop
   */
  animate() {
    requestAnimationFrame(() => this.animate());

    const delta = Math.min(this.clock.getDelta(), 0.1) * this.simSpeed;

    if (this.controls) this.controls.update();

    if (!this.isAutomationPaused) {
      this.updateAMRs(delta);
      this.updateElevators(delta);
    }
    // Humans keep moving even if AMR automation is halted!
    this.updateHumans(delta);

    // Update V2V Mesh Laser Lines
    if (this.showV2V) this.updateV2VMeshLines();

    // Spectator Camera
    if (this.spectatingBotId) {
      const mesh = this.robotMeshes.get(this.spectatingBotId);
      if (mesh) {
        const bot = this.robots.find(r => r.id === this.spectatingBotId);
        const h = bot ? bot.heading : 0;
        const targetX = mesh.position.x - Math.cos(h) * 7.5;
        const targetZ = mesh.position.z - Math.sin(h) * 7.5;
        const targetY = mesh.position.y + 4.5;

        this.camera.position.lerp(new THREE.Vector3(targetX, targetY, targetZ), 0.1);
        this.controls.target.lerp(mesh.position, 0.12);
      }
    }

    if (this.renderer && this.scene && this.camera) {
      this.renderer.render(this.scene, this.camera);
    }
  }

  updateAMRs(delta) {
    this.robots.forEach(bot => {
      if (bot.manualOverride) return;

      const mesh = this.robotMeshes.get(bot.id);
      if (!mesh) return;

      // Rotate LiDAR puck
      if (mesh.lidarRef) mesh.lidarRef.rotation.y += 14 * delta;

      // Update LED halo
      if (mesh.haloRef) {
        let col = 0x10b981; // Green
        if (bot.subState === 'REVERSING' || bot.subState === 'WAITING') col = 0xf59e0b;
        else if (bot.state === 'HALTED' || bot.ledStatus === 'RED') col = 0xef4444;
        mesh.haloRef.material.color.setHex(col);
      }

      this.stepBotNavigation(bot, delta);

      // Interpolate 3D position
      const targetPos = this.gridTo3D(bot.x, bot.y, bot.elevation || 0);
      mesh.position.x = THREE.MathUtils.lerp(mesh.position.x, targetPos.x, 0.25);
      mesh.position.y = THREE.MathUtils.lerp(mesh.position.y, targetPos.y, 0.25);
      mesh.position.z = THREE.MathUtils.lerp(mesh.position.z, targetPos.z, 0.25);
      mesh.rotation.y = THREE.MathUtils.lerp(mesh.rotation.y, -bot.heading, 0.25);
    });
  }

  stepBotNavigation(bot, delta) {
    if (bot.state === 'HALTED') return;

    if (bot.state === 'IDLE' && (!bot.path || bot.path.length === 0)) {
      if (Math.random() < 0.02) {
        this.assignAutonomousTask(bot);
      }
      return;
    }

    if (bot.path && bot.pathIndex < bot.path.length) {
      const nextNode = bot.path[bot.pathIndex];
      const dx = nextNode.x - bot.x;
      const dy = nextNode.y - bot.y;
      const dist = Math.hypot(dx, dy);

      const isReversing = bot.subState === 'REVERSING';
      const angle = Math.atan2(dy, dx);
      bot.heading = isReversing ? angle + Math.PI : angle;

      const speed = 2.2 * delta;
      bot.currentSpeed = 2.2;

      if (dist < speed) {
        bot.x = nextNode.x;
        bot.y = nextNode.y;
        bot.pathIndex++;

        if (bot.pathIndex >= bot.path.length) {
          this.handleTaskArrival(bot);
        }
      } else {
        bot.x += (dx / dist) * speed;
        bot.y += (dy / dist) * speed;
      }
    }
  }

  handleTaskArrival(bot) {
    if (bot.subState === 'ENTERING_BUFFER') {
      bot.state = 'BUFFER_OP';
      bot.currentSpeed = 0;
      if (window.app?.terminal) {
        window.app.terminal.logMove(bot.id, `Reached buffer face at (${bot.x}, ${bot.y}). Starting pick operation.`);
      }

      setTimeout(() => {
        // MANDATORY REVERSE-OUT PROTOCOL
        const waitingSpot = bot.targetRack?.waitingSpot || { x: bot.x, y: bot.y - 1 };
        bot.subState = 'REVERSING';
        bot.path = [{ x: waitingSpot.x, y: waitingSpot.y }];
        bot.pathIndex = 0;
        bot.state = 'NAVIGATING';
        if (window.app?.terminal) {
          window.app.terminal.logMove(bot.id, `Pick complete. Reversing out onto highway waiting cell (${waitingSpot.x}, ${waitingSpot.y}).`);
        }
      }, 1500);

    } else if (bot.subState === 'REVERSING') {
      if (bot.targetRack && bot.targetRack.bufferFace) {
        this.planner.releaseClaim(bot.targetRack.bufferFace.x, bot.targetRack.bufferFace.y, bot.id);
      }
      bot.subState = 'HIGHWAY';
      bot.state = 'IDLE';
      bot.targetRack = null;
      bot.path = [];
      if (window.app?.terminal) {
        window.app.terminal.logMove(bot.id, `Returned to Highway. Cell reservation released.`);
      }
    } else {
      bot.state = 'IDLE';
      bot.path = [];
    }
  }

  assignAutonomousTask(bot) {
    if (!this.racks || this.racks.length === 0) return;
    const targetRack = this.racks[Math.floor(Math.random() * this.racks.length)];
    if (!targetRack.bufferFace) return;

    const claim = this.planner.claimCell(targetRack.bufferFace.x, targetRack.bufferFace.y, bot.id);
    if (claim.success) {
      const curX = Math.round(bot.x);
      const curY = Math.round(bot.y);
      const path = this.planner.findHighwayPath(curX, curY, targetRack.waitingSpot.x, targetRack.waitingSpot.y, bot.id);
      if (path) {
        path.push({ x: targetRack.bufferFace.x, y: targetRack.bufferFace.y });
        bot.targetRack = targetRack;
        bot.path = path;
        bot.pathIndex = 0;
        bot.state = 'NAVIGATING';
        bot.subState = 'ENTERING_BUFFER';
        if (window.app?.terminal) {
          window.app.terminal.logMove(bot.id, `Dispatched to ${targetRack.id} (Buffer Face: ${targetRack.bufferFace.x}, ${targetRack.bufferFace.y})`);
        }
      }
    }
  }

  updateElevators(delta) {
    (this.elevators || []).forEach(elv => {
      if (elv.isMoving && elv.cabRef) {
        const targetY = elv.targetFloor === 2 ? 4.2 : 0;
        elv.cabRef.position.y = THREE.MathUtils.lerp(elv.cabRef.position.y, targetY, 0.05);
        if (Math.abs(elv.cabRef.position.y - targetY) < 0.05) {
          elv.isMoving = false;
          elv.currentFloor = elv.targetFloor;
        }
      }
    });
  }

  updateHumans(delta) {
    if (!this.showWorkers) return;

    this.humans.forEach(h => {
      if (h.manualOverride) return;

      const mesh = this.humanMeshes.get(h.id);
      if (!mesh) return;

      h.walkPhase = (h.walkPhase || 0) + 7 * delta;
      if (mesh.lLeg) mesh.lLeg.rotation.x = Math.sin(h.walkPhase) * 0.45;
      if (mesh.rLeg) mesh.rLeg.rotation.x = -Math.sin(h.walkPhase) * 0.45;

      if (h.path && h.path.length > 0) {
        const nextPt = h.path[h.pathIndex % h.path.length];
        const dx = nextPt.x - h.x;
        const dy = nextPt.y - h.y;
        const dist = Math.hypot(dx, dy);

        if (dist < 0.25) {
          h.pathIndex = (h.pathIndex + 1) % h.path.length;
        } else {
          const step = h.currentSpeed * delta;
          h.heading = Math.atan2(dy, dx);
          h.x += (dx / dist) * step;
          h.y += (dy / dist) * step;
        }

        const pos = this.gridTo3D(h.x, h.y, h.elevation || 0);
        mesh.position.x = pos.x;
        mesh.position.z = pos.z;
        mesh.rotation.y = -h.heading;
      }
    });
  }

  updateV2VMeshLines() {
    this.v2vMeshGroup.clear();
    const lineMat = new THREE.LineBasicMaterial({ color: 0x00e5ff, transparent: true, opacity: 0.35 });

    for (let i = 0; i < this.robots.length; i++) {
      for (let j = i + 1; j < this.robots.length; j++) {
        const b1 = this.robots[i];
        const b2 = this.robots[j];
        const dist = Math.hypot(b1.x - b2.x, b1.y - b2.y);

        if (dist < 18) { // C-V2X RF communication range
          const p1 = this.gridTo3D(b1.x, b1.y, (b1.elevation || 0) + 0.45);
          const p2 = this.gridTo3D(b2.x, b2.y, (b2.elevation || 0) + 0.45);

          const geo = new THREE.BufferGeometry().setFromPoints([
            new THREE.Vector3(p1.x, p1.y, p1.z),
            new THREE.Vector3(p2.x, p2.y, p2.z)
          ]);
          this.v2vMeshGroup.add(new THREE.Line(geo, lineMat));
        }
      }
    }
  }

  // Camera Presets
  setCameraMode(mode) {
    this.spectatingBotId = null;
    if (mode === 'orbit') {
      this.camera.position.set(0, 58, 68);
      this.controls.target.set(0, 0, 0);
    } else if (mode === 'isometric') {
      this.camera.position.set(50, 50, 50);
      this.controls.target.set(0, 0, 0);
    } else if (mode === 'topdown') {
      this.camera.position.set(0, 110, 0.1);
      this.controls.target.set(0, 0, 0);
    } else if (mode === 'follow') {
      this.spectatingBotId = 'AMR-01';
    }
  }

  // Overlays Toggles
  toggleLidar() {
    this.showLidar = !this.showLidar;
    this.robotMeshes.forEach(m => { if (m.laserRef) m.laserRef.visible = this.showLidar; });
    return this.showLidar;
  }
  togglePaths() {
    this.showPaths = !this.showPaths;
    this.pathLinesGroup.visible = this.showPaths;
    return this.showPaths;
  }
  toggleV2V() {
    this.showV2V = !this.showV2V;
    this.v2vMeshGroup.visible = this.showV2V;
    return this.showV2V;
  }
  toggleWorkers() {
    this.showWorkers = !this.showWorkers;
    this.humanMeshes.forEach(m => m.visible = this.showWorkers);
    return this.showWorkers;
  }

  pauseAutomation() {
    this.isAutomationPaused = true;
    this.robots.forEach(r => { r.currentSpeed = 0; r.ledStatus = 'RED'; });
  }

  resumeAutomation() {
    this.isAutomationPaused = false;
    this.robots.forEach(r => { r.ledStatus = 'GREEN'; });
  }

  setSimSpeed(s) { this.simSpeed = s; }

  sendBotToFloor(botId, targetFloor) {
    const bot = this.robots.find(r => r.id === botId);
    if (!bot) return;
    bot.floor = targetFloor;
    bot.elevation = targetFloor === 2 ? 4.2 : 0;
    if (window.app?.terminal) {
      window.app.terminal.logMove(botId, `Cargo elevator transfer complete. AMR operating on Floor ${targetFloor}.`);
    }
  }
}
