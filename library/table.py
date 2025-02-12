from db import Base
from sqlalchemy import Column, String, Integer

class Books(Base):
    __tablename__ = "Book_list"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    description = Column(String, index=True)
    year = Column(Integer, index=True)

