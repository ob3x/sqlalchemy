from db import Base
from sqlalchemy import Column, Integer, String, Boolean, Date

class BookingDB(Base):
    __tablename__ = "Halls"
    id = Column(Integer, primary_key=True, index=True)
    hall = Column(String)
    status = Column(Boolean)