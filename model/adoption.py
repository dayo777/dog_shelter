from datetime import datetime
from pydantic import BaseModel


class Adoption(BaseModel):
    id: int
    dogId: int
    adopter: str # TODO: make this relate to a volunteer
    adoptionDate: datetime
    status: str