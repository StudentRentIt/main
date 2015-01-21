import factory
from factory.django import DjangoModelFactory

from django.contrib.auth import get_user_model

from property.models import Property, PropertyFavorite
from school.models import Deal, Event, School, Neighborhood
from realestate.models import Company
from main.models import City, Contact
from blog.models import Tag, Article

User = get_user_model()



##### MAIN #####
class ContactFactory(DjangoModelFactory):

    class Meta:
        model = Contact

    first_name="Mr"
    last_name="Tester"
    email="tester@gmail.com"
    phone_number=1231231234
    subject="Test Subject"
    body="this is the contact body"


##### PROPERTY #####
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


##### SCHOOL #####
class SchoolFactory(DjangoModelFactory):
    # need to pass in city
    class Meta:
        model = School

    name="RE Test University"
    long=-97.1234123
    lat=45.7801234


class NeighborhoodFactory(DjangoModelFactory):
    # pass in school
    class Meta:
        model = Neighborhood

    name = "Test Neighborhood"
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


##### REAL ESTATE #####
class CompanyFactory(DjangoModelFactory):
    # need to pass in default_school
    class Meta:
        model = Company

    name="Test Company"


##### MAIN #####
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
    username = 'realestateuser'
    password = 'repassword'
    email = 're@email.com'
    first_name = 'Sir'
    last_name = 'Real Estate'



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


###### BLOG #####
class ArticleFactory(DjangoModelFactory):
    # pass in user, school, property
    class Meta:
        model = Article

    title="Test Article" 
    body="This is the body of the article."
    image=factory.django.ImageField(color='blue')


class TagFactory(DjangoModelFactory):
    # pass in title
    class Meta:
        model = Tag

