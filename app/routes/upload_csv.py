from fastapi import APIRouter, File, UploadFile, HTTPException
from app.database import db  # Assumes you have a db instance from PyMongo
import pandas as pd
import io

router = APIRouter()

@router.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed.")

    try:
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

        # Optional: Parse 'inspection_date' column to datetime if it exists
        if 'inspection_date' in df.columns:
            df["inspection_date"] = pd.to_datetime(df["inspection_date"])

        data = df.to_dict(orient="records")

        if not data:
            raise HTTPException(status_code=400, detail="CSV file is empty or invalid format.")
        
        db.gears.insert_many(data)

        return {"message": f"Successfully uploaded {file.filename}", "rows": len(data)}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing CSV: {str(e)}")
