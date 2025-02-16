from db import get_db
from schemas import CreateBooking, Booking
from models import BookingDB

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import uvicorn
from typing import Annotated

app = FastAPI()
db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/halls/", response_model=list[Booking])
def return_halls(db : db_dependency):
    rooms = db.query(BookingDB).order_by(BookingDB.id).all()

    if not rooms:
        raise HTTPException(status_code=404, detail="Error, halls not found")
    
    return rooms

@app.get("/available-halls/", response_model=list[Booking])
def available_halls(db : db_dependency):
    rooms = db.query(BookingDB).filter(BookingDB.status == True).order_by(BookingDB.id).all()

    if not rooms:
        raise HTTPException(status_code=404, detail="Error, halls not found")
    
    return rooms

@app.post("/add-hall/", response_model=Booking)
def add_hall(hall : CreateBooking, db : db_dependency):
    room = BookingDB(**hall.model_dump())
    db.add(room)
    db.commit()
    db.refresh(room)
    return room

@app.put("/booking-hall", response_model=Booking)
def booking_hall(hall_id : int, db : db_dependency):
    room = db.query(BookingDB).filter(BookingDB.id == hall_id).first()

    if not room:
        raise HTTPException(status_code=404, detail="Error, halls not found")
    
    room.status = False
    db.commit()
    db.refresh(room)
    return room


@app.delete("/delete-hall/", response_model=Booking)
def delete_hall(hall_id : int, db : db_dependency):
    room = db.query(BookingDB).filter(BookingDB.id == hall_id).first()

    if not room:
        raise HTTPException(status_code=404, detail="Error, halls not found")

    db.delete(room)
    db.commit()
    return room

if __name__ == "__main__":
    uvicorn.run(app)