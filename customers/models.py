from sqlalchemy import Column, String, Integer, Boolean
from db import Base

class CustomersDB(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    phone = Column(String)
    available = Column(Boolean)
    created_at = Column(String)

# class NotesDB(Base):
#     __tablename__ = "notes"
#     id = Column(Integer, primary_key=True, index=True)
#     customer_id = Column(Integer)
#     content = Column(String)
#     created_at = Column(String)