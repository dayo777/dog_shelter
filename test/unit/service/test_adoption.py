""" Test the Adoption service module """


from service import adoption as AdoptionService
from model.adoption import Adoption


sample_adoption = Adoption(
    id = "abc123",
    dogId = "123456",
    adopter = {
        "id": "xyz789",
        "name": "Jane Smith",
        "email": "jane.smith@example.com",
        "address": "1, Broad st, San francisco",
        "phone": "555-5678",
        "role": "Dog Walker",
        "startDate": "2022-06-01"
    },
    adoptionDate = "2023-04-15",
    status = "Completed"
)


def test_create():
    """ Confirm that create function creates valid data """
    resp = AdoptionService.create_volunteer(sample_adoption)
    assert resp == AdoptionService

def test_get_exists():
    """ Confirm that valid ID returns data """
    resp = AdoptionService.get_adoption(sample_adoption.id)
    assert resp == sample_adoption

def test_get_missing():
    """ Confirm that missing ID returns None """
    resp = AdoptionService.get_adoption(1000)
    assert resp is None