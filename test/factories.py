from django.contrib.auth import get_user_model

from factory.django import DjangoModelFactory

from property.models import Property, PropertyFavorite
from school.models import Deal, Event, School
from realestate.models import Company
from main.models import City

User = get_user_model()


class PropertyFactory(DjangoModelFactory):
    # pass in school, user, real_estate_company
    class Meta:
        model = Property

    title="test property"
    addr="13 Test St."
    city="Test Town"
    state="TX"


class FavoriteFactory(DjangoModelFactory):
    # pass in property, user
    class Meta:
        model = PropertyFavorite

    note="test note"


class SchoolFactory(DjangoModelFactory):
    # need to pass in city
    class Meta:
        model = School

    name="RE Test University"
    long=-97.1234123
    lat=45.7801234


class DealFactory(DjangoModelFactory):
    # pass in school, property, user
    class Meta:
        model = Deal

    title="test deal"
    description="This is the deal object created in testing"


class EventFactory(DjangoModelFactory):
    # pass in school, user
    class Meta:
        model = Event

    title="test event"
    description="this is the test event object"
    location="somewhere yonder"


class CompanyFactory(DjangoModelFactory):
    # need to pass in default_school
    class Meta:
        model = Company

    name="Test Company"


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User


class NormalUserFactory(UserFactory):
    username = 'normaluser'
    password = 'normalpassword'
    email = 'user@email.com'
    first_name = 'John'
    last_name = 'Doe'


class RealEstateUserFactory(UserFactory):
    # pass in real_estate_company
    username = 'bloguser'
    password = 'blogpassword'
    email = 'blog@email.com'
    first_name = 'Sir'
    last_name = 'Blogger'



class StaffUserFactory(UserFactory):
    username = 'staffuser'
    password = 'staffpassword'
    email = 'staff@email.com'
    first_name = 'Staff'
    last_name = 'User'
    is_staff = True


class AdminUserFactory(UserFactory):
    username = 'adminuser'
    password = 'adminpassword'
    email = 'admin@email.com'
    first_name = 'Admin'
    last_name = 'User'
    is_staff = True
    is_superuser = True


class CityFactory(DjangoModelFactory):
    class Meta:
        model = City

    name = "Test Town"
    state = "TX"