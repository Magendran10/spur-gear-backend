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

        def parse_date(s: str):
            try:
                return datetime.fromisoformat(s.replace("Z", "+00:00"))
            except Exception:
                return None

        # Fetch all data and filter in Python
        all_gears = list(db.gears.find())
        result = []
        for gear in all_gears:
            if "inspection_date" in gear:
                inspection_dt = parse_date(gear["inspection_date"])
                if inspection_dt and start <= inspection_dt <= end:
                    gear["_id"] = str(gear["_id"])
                    gear["inspection_date"] = inspection_dt.isoformat()
                    result.append(gear)

        return result

    except Exception as e:
        return {"error": str(e)}
