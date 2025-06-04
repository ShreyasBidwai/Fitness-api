from pydantic import BaseModel, EmailStr
from typing import List
from datetime import datetime


class FitnessClass(BaseModel):
    id: int
    name: str
    datetime: datetime
    instructor: str
    available_slots: int


class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr


class Booking(BaseModel):
    class_id: int
    client_name: str
    client_email: EmailStr
    class_name: str
    datetime: datetime
    instructor: str
