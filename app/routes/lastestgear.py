from fastapi import APIRouter
from app.database import db

router = APIRouter()

@router.get("/latest-gears")
def get_latest_gears():
    collection = db["gears"]
    gears = list(collection.find().sort("_id", -1).limit(1))  # get latest 10 records
    for gear in gears:
        gear["_id"] = str(gear["_id"])  # Convert ObjectId to string
    return gears

