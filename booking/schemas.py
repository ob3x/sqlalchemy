from pydantic import BaseModel

class BaseBooking(BaseModel):
    hall : str = "hall"
    status : bool = True

class CreateBooking(BaseBooking):
    pass

class Booking(BaseBooking):
    id : int

    class Config:
        orm_mode = True
        from_attribute = True