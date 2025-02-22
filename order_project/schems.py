from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class OrderItemModel(BaseModel):
    name : str
    price : int

class OrderItemCreate(OrderItemModel):
    pass

class OrderItem(OrderItemModel):
    id : int
    order_id : int

    class Config:
        from_attributes = True

class OrderModel(BaseModel):
    pass

class OrderCreate(OrderModel):
    items: List[OrderItemCreate] = []

class Order(OrderModel):
    id : int
    created_at : datetime
    items : List[OrderItem] = []

    class Config:
        from_attributes = True