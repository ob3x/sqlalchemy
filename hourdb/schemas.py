from pydantic import BaseModel
from datetime import datetime

class HoursBase(BaseModel):
    hour : str

class CreateHours(HoursBase):
    pass

class Hours(HoursBase):
    id : int

    class Config:
        orm_mode = True
        from_attribute = True