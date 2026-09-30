"""
FastAPI + WebSocket Live Warehouse Viewer Server
Unified Edge-AI Distributed Fleet Coordination for AMRs
"""
import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from routers import core, diagnostics, faults, humans, returns_kiva, slotting, telemetry, rooms

app = FastAPI(
    title="Edge AMR Fleet Visualizer API",
    description="Decentralized Fleet Coordination Backend for Autonomous Mobile Robots",
    version="2.0.0"
)

# Enable CORS for Firebase frontend and local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount public directory and assets if present
public_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "public"))
if os.path.exists(public_dir):
    js_dir = os.path.join(public_dir, "js")
    css_dir = os.path.join(public_dir, "css")
    if os.path.exists(js_dir):
        app.mount("/js", StaticFiles(directory=js_dir), name="js")
    if os.path.exists(css_dir):
        app.mount("/css", StaticFiles(directory=css_dir), name="css")
    app.mount("/static", StaticFiles(directory=public_dir), name="static")

    @app.get("/map.json")
    async def get_map_json():
        from fastapi.responses import FileResponse
        map_file = os.path.join(public_dir, "map.json")
        if os.path.exists(map_file):
            return FileResponse(map_file)
        return {"error": "map.json not found"}

# Mount all feature routers
for module in (core, telemetry, faults, humans, diagnostics, slotting, returns_kiva, rooms):
    app.include_router(module.router)

@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "amr3d-backend", "version": "2.0.0"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, log_level="info")
