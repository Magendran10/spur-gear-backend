from fastapi import APIRouter
from app.database import db
router = APIRouter()

@router.post("/detect")
def save_detection(data: dict):
    db.gears.insert_one(data)
    return {"status": "saved"}
