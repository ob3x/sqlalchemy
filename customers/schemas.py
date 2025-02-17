from pydantic import BaseModel
from datetime import datetime

class BaseCustomers(BaseModel):
    name : str
    surname : str
    email : str
    phone : str
    available : bool = True
    created_at : str

class CreateCustomers(BaseCustomers):
    pass

class Customers(BaseCustomers):
    id : int

    class Config:
        orm_mode = True