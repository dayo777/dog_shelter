from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class Volunteer(BaseModel):
    id: int
    name: str = Field(...)
    email: EmailStr = Field(...)
    phone: str
    role: str = Field(...)
    startDate: datetime