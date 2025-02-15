from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import uvicorn
from schemas import CreateHours, Hours
import tables
from db import get_db
from datetime import datetime

app = FastAPI()

@app.post("/post-hours/", response_model=Hours)
def post_hour(hour : CreateHours, db : Session = Depends(get_db)):
    hour.hour = datetime.now().strftime("%H:%M:%S")
    hours_db = tables.HoursDB(**hour.model_dump())
    db.add(hours_db)
    db.commit()
    db.refresh(hours_db)
    return hours_db

@app.get("/hours/", response_model=list[Hours])
def get_hour(db : Session = Depends(get_db)):
    return db.query(tables.HoursDB).all()

@app.delete("/remove-hours/{hero_id}", response_model=Hours)
def remove_hour(hour_id : int, db : Session = Depends(get_db)):
    hour_to_delete = db.query(tables.HoursDB).filter(tables.HoursDB.id == hour_id).first()
    if not hour_to_delete:
        raise HTTPException(status_code=404, detail="Error, id not found")
    db.delete(hour_to_delete)
    db.commit()

    return hour_to_delete



if __name__ == "__main__":
    uvicorn.run(app)