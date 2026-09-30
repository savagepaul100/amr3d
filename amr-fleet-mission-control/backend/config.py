"""Paths and constants shared across the server."""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PUBLIC_DIR = BASE_DIR.parent / "public"

STATIC_DIR = PUBLIC_DIR if PUBLIC_DIR.exists() else (BASE_DIR / "static")
INDEX_HTML = (PUBLIC_DIR / "index.html") if (PUBLIC_DIR / "index.html").exists() else (BASE_DIR / "templates" / "index.html")

HOST = os.environ.get("HOST", "0.0.0.0")
PORT = int(os.environ.get("PORT", 8000))

WAREHOUSE_WIDTH = 170
WAREHOUSE_HEIGHT = 50
FLOORS_PER_RACK = 5
