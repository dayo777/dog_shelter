from ast import List
from fastapi import APIRouter, HTTPException
from error import Duplicate, Missing
from data import volunteer as service
from model.volunteer import Volunteer



router = APIRouter()

@router.get("")
@router.get("/")
def list() -> list[Volunteer]:
    return service.list_volunteer()

@router.get("/{id}")
def get(id: int) -> Volunteer:
    pass

@router.post("", status_code=201)
@router.post("/", status_code=201)
def create(volunteer: Volunteer) -> Volunteer:
    try:
        return service.create_volunteer(volunteer)
    except Duplicate as err:
        raise HTTPException(status_code=404, detail=err.msg)

@router.patch("/{id}")
def update(id: int, volunteer: Volunteer) -> Volunteer:
    try:
        return service.update_volunteer(id, volunteer)
    except Missing as err:
        raise HTTPException(status_code=404, detail=err.msg)

@router.delete("/{id}", status_code=204)
def delete(id: int):
    try:
        return service.delete_volunteer(id)
    except Missing as err:
        raise HTTPException(status_code=404, detail=err.msg)