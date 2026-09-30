"""
Room Management and Offline Delta Engine Router
"""
import time
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional

router = APIRouter(prefix="/api/rooms", tags=["Rooms"])

# In-memory storage for active rooms
ROOMS_STORE: Dict[str, Dict[str, Any]] = {}

class RoomSaveRequest(BaseModel):
    room_id: str
    data: Dict[str, Any]

@router.get("/{room_id}")
async def get_room(room_id: str):
    if room_id in ROOMS_STORE:
        room = ROOMS_STORE[room_id]
        # Calculate offline delta catchup
        now = time.time()
        last_updated = room.get("lastUpdated", now)
        elapsed = max(0, min(86400, now - last_updated))
        room["elapsedSeconds"] = elapsed
        return room
    return {"id": room_id, "status": "not_cached"}

@router.post("/save")
async def save_room(payload: RoomSaveRequest):
    data = payload.data
    data["lastUpdated"] = time.time()
    ROOMS_STORE[payload.room_id] = data
    return {"status": "saved", "room_id": payload.room_id, "timestamp": data["lastUpdated"]}
