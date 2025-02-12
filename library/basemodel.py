from pydantic import BaseModel

class BookBase(BaseModel):
    title : str
    author : str
    description : str
    year : int = 2025

class CreateBook(BookBase):
    pass

class Book(BookBase):
    id : int

    class config:
        orm_mode = True
        from_attribute = True