from pydantic import BaseModel
from datetime import datetime

class BookingCreate(BaseModel):
    room_id: int
    start_date: datetime
    end_date: datetime

class BookingOut(BookingCreate):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True