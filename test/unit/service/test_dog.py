""" Test the Dog service module """


from model.dog import Dog
from service import dog as DogService



sample_dog = Dog(
        id = 1,
        name = "Buddy",
        breed = "Labrador Retriever",
        age = 5,
        gender = "male",
        size = "Large",
        color = "white",
        description = "Friendly and enegertic dog",
        status = "Available",
        adoptionDate = None,
        adoptionFee = 20.5,
        created_at = "2024-10-09",
        updated_at = None
    )

def test_create():
    """ Confirm that create function creates valid data """
    resp = DogService.create_dog(sample_dog)
    assert resp == sample_dog

def test_get_exists():
    """ Confirm that valid ID returns data """
    resp = DogService.get_dog(sample_dog.id)
    assert resp == sample_dog

def test_get_missing():
    """ Confirm that missing ID returns None """
    resp = DogService.get_dog(1000)
    assert resp is None