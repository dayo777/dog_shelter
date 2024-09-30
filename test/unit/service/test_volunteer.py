""" Test the Dog service module """


from model.volunteer import Volunteer
from service import volunteer as VolunteerService

sample_volunteer = Volunteer(
        id = 1,
        name = "Jane Smith",
        email = "Jane.smith@example.com",
        address = "1, Broad st, San francisco",
        phone = "555-5678",
        role = "Dog walker",
        startDate = "2024-10-10 12:20"
)


def test_create():
    """ Confirm that create function creates valid Volunteer data """
    resp = VolunteerService.create_volunteer(sample_volunteer)
    assert resp == sample_volunteer

def test_get_exists():
    """ Confirm that valid ID returns data """
    resp = VolunteerService.get_volunteer(sample_volunteer.id)
    assert resp == sample_volunteer

def test_get_missing():
    """ Confirm that missing ID returns None """
    resp = VolunteerService.get_volunteer(1000)
    assert resp is None