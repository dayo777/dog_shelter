from datetime import datetime
from pydantic import BaseModel


class Volunteer(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    role: str
    startDate: datetime