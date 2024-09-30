from fastapi import APIRouter, HTTPException

from error import Duplicate, Missing
from model.adoption import Adoption
from model.dog import Dog
from data import adoption as service


router = APIRouter()

@router.get("")
@router.get("/")
def list() -> list[Adoption]:
    """Return a list of all the adoptions"""
    return service.list_adoption()

@router.post("", status_code=201)
@router.post("/", status_code=201)
def create(adoption: Adoption) -> Adoption:
    """Create an Adoption resource"""
    try:
        return service.create_adoption(adoption)
    except Duplicate as err:
        raise HTTPException(status_code=404, detail=err.msg)

@router.get("/{id}")
def get(id: int) -> Adoption:
    try:
        return service.get_adoption(id)
    except Missing as err:
        raise HTTPException(status_code=404, detail=err.msg)

@router.patch("/{id}")
def update(id: int, adoption: Adoption) -> Dog:
    try:
        return service.update_adoption(id, adoption)
    except Missing as err:
        raise HTTPException(status_code=404, detail=err.msg)

@router.delete("/{id}", status_code=204)
def delete(id: int):
    try:
        return service.delete_adoption(id)
    except Missing as err:
        raise HTTPException(status_code=404, detail=err.msg)