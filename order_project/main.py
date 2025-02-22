from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from models import Order, OrderItem
from db import get_db
import schems

app = FastAPI()

@app.post("/add-order", response_model=schems.Order)
def add_order(order : schems.OrderCreate, db : Session = Depends(get_db)):
    new_order = Order(**order.model_dump())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    for item in order.items:
        new_item = OrderItem(order_id = new_order.id, **item.model_dump())
        db.add(new_item)

    db.commit()
    db.refresh(new_order)
    return new_order


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)