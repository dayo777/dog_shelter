from pydantic import BaseModel, Field
from pydantic.functional_validators import BeforeValidator
from datetime import datetime
from typing import List
from typing_extensions import Annotated
from bson import ObjectId


PyObjectId = Annotated[str, BeforeValidator(str)]

class Dog(BaseModel):
    """
    Container for a single Dog record
    """
    # id: Optional[PyObjectId] = Field(alias="_id", default=None)
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
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra ={
            "example": {
                "name": "Buddy",
                "breed": "Labrador Retriever",
                "age": 5,
                "gender": "Male",
                "description": "Friendly and energetic dog",
                "status": "Available",
                "adoptionDate": "2024-10-01 12:00",
                "adoptionFee":  20.5,
                "updated_at": "2024-10-01 12:00"
            }
        }


class DogCollection(BaseModel):
    """
    This exists because providing a top-level array in a JSON response
    can be a [vulnerability](https://haacked.com/archive/2009/06/25/json-hijacking.aspx/)
    """
    students: List[Dog]
