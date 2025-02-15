from sqlalchemy import Column, Integer, String, Boolean
from db import Base

class TodosDB(Base):
    __tablename__ = "Todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    hour = Column(String)
    description = Column(String)
    edited = Column(Boolean)