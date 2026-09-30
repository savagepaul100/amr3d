# AMR Fleet Mission Control - Interactive 3D Digital Twin

[![Live Demo](https://img.shields.io/badge/Live%20Demo-amr3d.web.app-38bdf8?style=for-the-badge&logo=google-chrome&logoColor=white)](https://amr3d.web.app)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Three.js](https://img.shields.io/badge/Three.js-r128-000000?style=for-the-badge&logo=three.js&logoColor=white)](https://threejs.org)
[![ISO 3691-4](https://img.shields.io/badge/Safety-ISO%203691--4%20Compliant-ef4444?style=for-the-badge)](https://www.iso.org/standard/69599.html)

A high-fidelity **3D Digital Twin and Mission Control Suite** for autonomous warehouse logistics featuring Autonomous Mobile Robots (AMRs), 5-tier storage racks, diverse human workers, dynamic obstacle avoidance, decentralized V2V communication mesh, and interactive tele-operation.

---

## 🌟 Key Features

### 1. Dual Viewport: 3D Digital Twin & 2D Tactical Grid
- **3D Industrial Environment**: Built on Three.js with realistic lighting, shadows, instanced meshes for 1,500+ rack pods, and real-time rendering.
- **Choreographed 2D $\leftrightarrow$ 3D Transitions**:
  - **3D $\to$ 2D**: Smoothly zooms out $\to$ camera moves directly overhead to match 2D layout $\to$ cross-fades into 2D canvas $\to$ zooms in on spectated/controlled robot.
  - **2D $\to$ 3D**: 2D zooms out to full overview $\to$ 3D camera aligns overhead $\to$ smoothly glides down into signature isometric angle.
- **Synchronized State**: All robot positions, headings, cargo loads, and worker routes are updated simultaneously in both 2D and 3D.

### 2. Autonomous Mobile Robots (AMRs)
- **Authentic Robot Models**: Dual drive wheels, swivel casters, front 360° LiDAR puck with active laser beam sweeps, and status LED halos.
- **Dynamic Scissor-Lift Cargo Deck**: Deck lowers to $0.44\,\text{m}$ when unladen and elevates to $0.62\,\text{m}$ with realistic movement inertia and vibration when carrying cargo.
- **Consistent Freight Parcels**: Golden-yellow (`#facc15`) freight cartons that appear uniformly on robot decks, warehouse floors, and rack shelves.
- **Decentralized V2V Mesh**: Peer-to-peer 5.9 GHz C-V2X communication links ($r=22\,\text{m}$) visualized as electric cyan RF lines with pulsing packet exchanges.

### 3. ISO 3691-4 Safety & Dynamic Obstacle Avoidance
- **Human Workforce**: Animated male and female safety auditors and inventory specialists with realistic walking cycles and inspection routes.
- **Safety Zones**:
  - **Emergency Braking Zone ($<1.8\,\text{m}$)**: Autonomous Emergency Braking (AEB) yields absolute priority to humans.
  - **Caution Slow Zone ($1.8\,\text{m} - 3.5\,\text{m}$)**: Smooth deceleration to 35% speed.
  - **Dynamic A\* Rerouting**: If path is obstructed for $>1.5\,\text{s}$, AMRs automatically plan alternative paths around obstacles.
- **Obstacle Variety**: Hazard safety cones with pulsating amber beacons, staging pallet carts with wooden decks and steel corner brackets, and dropped floor cartons.

### 4. Interactive Tele-Operation (WASD)
- **Direct Control**: Right-click any AMR or human worker and select **"Take Control"**.
- **Camera Perspectives (Toggle with `V`)**:
  - **3rd Person**: Dynamic chase camera following behind the robot.
  - **Close-Up**: Forward hood/sensor perspective.
  - **Free Move**: Detached orbit camera for overview while driving.
- **Physical Cargo Pick & Drop (Key `E` or `F`)**:
  - Near a floor box: Picks up the box and elevates the scissor deck.
  - Near a rack: Directly places cargo into the lowest available tier shelf.
  - Open floor: Drops carton onto the floor (with a 3.5s drive-away collision grace period).
- **Dock & Fast Charge (Key `C`)**: Instantly docks to nearest charger when within $2.0\,\text{m}$.
- **Battery Simulation**: Driving in manual mode consumes battery; reaching 0% triggers safe shutdown and dispatches an autonomous AGV recovery tug.

### 5. Dual Terminal Consoles & Spawner
- **Terminal 1 (Live Stream)**: Real-time mission events, telemetry, battery warnings, and safety yields.
- **Terminal 2 (CLI Boss)**: Interactive command prompt supporting commands:
  - `add <amr|worker|rack|parcel|hurdle|cart> [x] [y]`
  - `halt [all|id]` / `run [all|id]`
  - `set batt <id> <0-100>` / `set speed <id> <val>`
  - `spec <id>` / `find <id>`
- **Raycast Context Menu**: Right-click anywhere in 2D or 3D view to inspect exact grid coordinates and spawn entities directly on the floor.

---

## 📁 Repository Structure

```
.
├── backend/                  # FastAPI fleet coordination backend
│   ├── routers/              # Feature endpoints (telemetry, faults, humans, slotting, etc.)
│   ├── config.py             # Server paths and configuration
│   ├── inventory.py          # Warehouse SKU and parcel management
│   ├── main.py               # Application entrypoint & static mount
│   ├── models.py             # Pydantic data schemas
│   ├── requirements.txt      # Python dependencies
│   ├── services.py           # Shared state services
│   ├── state.py              # WebSocket connection state
│   └── warehouse_map.py      # Grid map topology generator
├── public/                   # Production frontend (deployed to Firebase)
│   ├── index.html            # Main visualizer application
│   ├── map.json              # Warehouse grid topology & nodes
│   ├── css/
│   │   └── industrial.css    # High-contrast dark styling
│   └── js/
│       ├── app.js            # Frontend orchestrator
│       ├── captcha.js        # Warehouse ID verification modal
│       ├── engine3d.js       # Three.js 3D world, lighting & models
│       ├── manual_control.js # WASD tele-operation system
│       ├── mission-control-enhancements.js # Master enhancement suite
│       ├── OrbitControls.js  # Camera controls
│       ├── planner.js        # A* pathfinding & detour logic
│       ├── room_manager.js   # Multi-room & fleet management
│       ├── tactical2d.js     # HTML5 Canvas 2D renderer
│       ├── terminal_boss.js  # Interactive CLI console
│       └── three.min.js      # Three.js library
├── assemble_master_js.py     # Build script for mission-control-enhancements.js
├── firebase.json             # Firebase Hosting deployment config
├── .firebaserc               # Firebase project target
├── render.yaml               # Render cloud deployment specification
├── .gitignore                # Git ignore rules
└── README.md                 # Project documentation
```

---

## 🚀 Quick Start Guide

### Option 1: Run Full-Stack with Python (Recommended)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/amr-fleet-mission-control.git
   cd amr-fleet-mission-control
   ```

2. **Set up Python virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r backend/requirements.txt
   ```

4. **Launch the server**:
   ```bash
   python backend/main.py
   ```

5. **Open in browser**:
   Navigate to [http://localhost:8000](http://localhost:8000).

---

### Option 2: Run Frontend Only (Static Web Server)

Since the frontend is a complete, self-contained client-side digital twin, you can serve the `public/` directory with any static server:

```bash
# Using Python:
cd public && python -m http.server 3000

# Or using Node.js:
npx serve public
```
Open [http://localhost:3000](http://localhost:3000) in your browser.

---

### Option 3: Deploy to Firebase Hosting

```bash
# Install Firebase CLI
npm install -g firebase-tools

# Login to Firebase
firebase login

# Deploy hosting
firebase deploy --only hosting
```

---

## 🎮 Controls & Keyboard Shortcuts

| Input | Action | Scope |
| :--- | :--- | :--- |
| **`W` / `A` / `S` / `D`** | Drive Forward / Steer Left / Reverse / Steer Right | Manual Control |
| **`V`** | Cycle Camera Mode (3rd Person $\to$ Close-up $\to$ Free Move) | Manual Control (3D) |
| **`V`** | Toggle Camera Follow / Free Pan | Manual Control (2D) |
| **`E` or `F`** | Pick Up / Drop Freight Carton | Manual Control (AMR) |
| **`C`** | Auto-Dock into Nearest Fast Charger ($<2\,\text{m}$) | Manual Control (AMR) |
| **Space** | Emergency Brake / Halt Momentum | Manual Control |
| **Left Click + Drag** | Orbit 3D Camera around focal point | 3D Viewport |
| **Right Click + Drag** | Pan 3D Camera across warehouse floor | 3D Viewport |
| **Mouse Wheel** | Zoom In / Out | 2D and 3D Viewports |
| **Right Click on Object** | Open Context Menu (Telemetry, Take Control, Follow) | Any Entity |
| **Right Click on Floor** | Open Coordinate Spawner Menu (AMR, Worker, Rack, Parcel, Cone, Cart) | Warehouse Floor |

---

## 🛠️ CLI Boss Commands (Terminal 2)

Type `help` in the Interactive Terminal to view the full command set:

- `add amr [x] [y]` — Spawn an autonomous AMR at coordinates.
- `add worker [x] [y] [male|female]` — Spawn a human warehouse specialist.
- `add rack [x] [y]` — Install a 5-tier storage rack with parcel inventory.
- `add parcel [x] [y]` — Stage a physical freight carton on the floor.
- `add hurdle [x] [y]` — Place an ISO safety cone hazard.
- `add cart [x] [y]` — Place a pallet staging cart.
- `halt all` / `halt <id>` — Emergency stop fleet or specific robot.
- `run all` / `run <id>` — Resume autonomous operation.
- `set batt <id> <0-100>` — Set battery state of charge.
- `set speed <id> <val>` — Modify robot cruising speed.
- `spec <id>` — Follow robot in 3D camera.
- `clear` — Clear terminal console output.

---

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.
