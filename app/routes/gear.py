from fastapi import APIRouter
from app.database import db

router = APIRouter()

@router.get("/gears")
def get_gears():
    gears = list(db.gears.find())
    for gear in gears:
        gear["_id"] = str(gear["_id"])  # convert ObjectId to string
    return gears
