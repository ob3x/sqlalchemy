from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from db import get_db
from schemas import CreateCustomers, Customers
from models import CustomersDB
from datetime import datetime

app = FastAPI()

@app.get("/get-customers", response_model=list[Customers])
def get_customers(db : Session = Depends(get_db)):
    customers = db.query(CustomersDB).order_by(CustomersDB.id).all()
    return customers


@app.post("/add-customers", response_model=Customers)
def add_customers(customer : CreateCustomers, db : Session = Depends(get_db)):
    new_customer = CustomersDB(**customer.model_dump())
    new_customer.created_at = datetime.now().strftime("%H:%M:%S")
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

@app.put("/edit-customers", response_model=Customers)
def edit_customers(customer_id : int, customer : CreateCustomers, db : Session = Depends(get_db)):
    edit_customer = db.query(CustomersDB).filter(customer_id == CustomersDB.id).first()

    if not customer:
        raise HTTPException(status_code=404, detail="Error, customer not found")

    edit_customer.name = customer.name
    edit_customer.surname = customer.surname
    edit_customer.email = customer.email
    edit_customer.phone = customer.phone
    edit_customer.name = customer.name
    db.commit()
    db.refresh(edit_customer)
    return edit_customer

# @app.put("/change-status")

@app.delete("/delete-customers", response_model=Customers)
def delete_customers(customer_id : int, db : Session = Depends(get_db)):
    customer = db.query(CustomersDB).filter(customer_id == CustomersDB.id).first()

    if not customer:
        raise HTTPException(status_code=404, detail="Error, customer not found")
    db.delete(customer)
    db.commit()
    return customer



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)