from pydantic import BaseModel

class TodosBase(BaseModel):
    title : str
    hour : str
    description : str
    edited : bool = False

class TodosCreate(TodosBase):
    pass

class Todos(TodosBase):
    id : int

    class Config:
        orm_mode = True
        from_attribute = True
