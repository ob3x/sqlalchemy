from sqlalchemy import Column, String, Integer
from db import Base

class HoursDB(Base):
    __tablename__ = "Hours_list"
    id = Column(Integer, primary_key=True, index=True)
    hour = Column(String, index=True)