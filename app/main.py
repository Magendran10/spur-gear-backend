from fastapi import FastAPI
from app.routes import gear
from app.routes import upload_csv
from app.routes import lastestgear
from app.routes import history
from app.routes import add
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# ✅ Add CORS middleware FIRST
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Safer than "*"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Then add routers
app.include_router(gear.router, prefix="/api")
app.include_router(lastestgear.router, prefix="/api")
app.include_router(upload_csv.router, prefix="/api")
app.include_router(history.router, prefix="/api")
app.include_router(add.router, prefix="/api")

# Static image mount
if not os.path.exists("images"):
    os.mkdir("images")
app.mount("/images", StaticFiles(directory="images"), name="images")
