from pydantic import BaseModel, Field
from datetime import datetime


class Dog(BaseModel):
    id: int
    name: str = Field(...)
    breed: str = Field(...)
    age: int = Field(...)
    gender: str = Field(...)
    description: str = Field(...)
    status: str = Field(...)
    adoptionDate: str | None = None
    adoptionFee: float = Field(...)
    created_at: datetime = Field(...)
    updated_at: datetime | None = None

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "_id": 1,
                "name": "Buddy",
                "breed": "Labrador Retriever",
                "age": 5,
                "gender": "Male",
                "description": "Friendly and energetic dog",
                "status": "Available",
                "adoptionDate": "2024-10-01 12:00",
                "adoptionFee":  20.5,
                "created_at": "2024-10-01 12:00",
                "updated_at": "2024-10-01 12:00"
            }
        }


class DogUpdate(BaseModel):
    name: str | None = None
    breed: str | None = None
    age: int | None = None
    gender: str | None = None
    description: str | None = None
    status: str | None = None
    adoptionDate: str | None = None
    adoptionFee: float | None = None
    updated_at: datetime | None = None

    class Config:
        json_schema_extra ={
            "example": {
                "name": "Buddy",
                "breed": "Labrador Retriever",
                "age": 5,
                "gender": "Male",
                "description": "Friendly and energetic dog",
                "status": "Available",
                "adoptionDate": None,
                "adoptionFee":  20.5,
                "created_at": "2024-10-01 12:00",
                "updated_at": None
            }
        }
