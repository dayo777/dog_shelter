from ast import List
from fastapi import APIRouter, HTTPException, status, Request, Body, Response
from data import dog as db_service
from model.dog import Dog, DogUpdate
from error import Duplicate, Missing


router = APIRouter()

@router.get("", response_description="List all dogs")
@router.get("/", response_description="List all dogs")
def list(request: Request) -> list[Dog]:
    """Endpoint to return a list of dogs"""
    return db_service.list_dog(request)

@router.get("/{id}", response_description="Get a single dog by id")
def get(id: str, request: Request) -> Dog:
    """Retrieve a single dog"""
    try:
        return db_service.get_dog(id, request)
    except Missing as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=err.msg)

@router.post("", status_code=status.HTTP_201_CREATED, response_description="Create a new dog.", response_model=Dog)
@router.post("/", status_code=status.HTTP_201_CREATED, response_description="Create a new dog.", response_model=Dog)
def create(request: Request, dog: Dog = Body(...)) -> Dog:
    """Create a Dog resource route"""
    try:
        return db_service.create_dog(request, dog)
    except Duplicate as err:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=err.msg)

@router.put("/{id}", response_description="Update a Dog", response_model=Dog)
def update(id: str, request: Request, dog: DogUpdate = Body(...)) -> Dog:
    try:
        return db_service.update_dog(id, request, dog)
    except Missing as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=err.msg)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_description="Delete a dog")
def delete(id: str, request: Request, response: Response):
    try:
        return db_service.delete_dog(id, request, response)
    except Missing as err:
        raise HTTPException(status_code=404, detail=err.msg)