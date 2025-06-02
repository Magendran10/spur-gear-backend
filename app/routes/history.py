from fastapi import APIRouter, Query
from app.database import db
from datetime import datetime
from typing import List

router = APIRouter()

@router.get("/history")
def get_history(start_date: str = Query(...), end_date: str = Query(...)):
    try:
        start = datetime.fromisoformat(start_date)
        end = datetime.fromisoformat(end_date)

        def parse_date(s):
            try:
                return datetime.fromisoformat(s)
            except ValueError:
                # Remove timezone if any
                return datetime.fromisoformat(s.split("+")[0])

        result = [
            gear for gear in db
            if "inspection_date" in gear and start <= parse_date(gear["inspection_date"]) <= end
        ]
        return result
    except Exception as e:
        return {"error": str(e)}
