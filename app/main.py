from fastapi import FastAPI
from app.routes import gear
from app.routes import upload_csv  # your new CSV upload router
from app.routes import lastestgear
from app.routes import history
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

app.include_router(gear.router, prefix="/api")


app.include_router(lastestgear.router, prefix="/api")

app.include_router(upload_csv.router, prefix="/api")
app.include_router(history.router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or your React dev server URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Assuming gear images are in a folder called 'images'
if not os.path.exists("images"):
    os.mkdir("images")

app.mount("/images", StaticFiles(directory="images"), name="images")




