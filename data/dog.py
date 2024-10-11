"""Table id is `dog`"""

from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, Request, status, Response
from model.dog import Dog, DogUpdate
from typing import List



def get_dog(id: int, request: Request) -> Dog:
    if (dog := request.app.database["dog"].find_one({"id": id})) is not None:
        return dog
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Dog with `{id}` not found.")

def create_dog(request: Request, dog: Dog) -> Dog:
    dog = jsonable_encoder(dog)
    new_dog = request.app.database["dog"].insert_one(dog)
    created_dog = request.app.database["dog"].find_one(
        {"_id": new_dog.inserted_id}
    )
    return created_dog

def list_dog(request: Request) -> List[Dog]:
    dogs = list(request.app.database["dog"].find(limit=50))
    return dogs

def update_dog(id: str, request: Request, dog: DogUpdate) -> Dog:
    dog = {k: v for k, v in dog.dict().items() if v is not None}
    if len(dog) >= 1:
        update_result = request.app.database["dog"].update_one(
            {"id": id}, {"$set": dog}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Dog with id {id} not found.")
    
    if (existing_dog := request.app.database["dog"].find_one({"id": id})) is not None:
        return existing_dog
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"Book with id `{id}` not found.")

def delete_dog(id: int, request: Request, response: Response):
    delete_result = request.app.database["dog"].delete_one({"id": id})
    if delete_result == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book '{id}' not found.")