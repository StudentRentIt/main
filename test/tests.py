from django.contrib.auth import get_user_model
from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from main.models import City, Payment, TeamMember, Contact
from school.models import School, Deal, Event
from realestate.models import Company
from property.models import Property, PropertyFavorite

from .factories import FavoriteFactory, PropertyFactory, DealFactory, EventFactory, \
                       SchoolFactory, CompanyFactory, CityFactory


class UserSetup(object):
    def setUp(self):
        self.User = get_user_model()

        # set up all types of users to be used
        self.staff_user = self.User.objects.create_user(
            'staff_user', 
            'staff@gmail.com', 
            'testpassword'
        )
        self.staff_user.is_staff = True
        self.staff_user.save()

        self.user = self.User.objects.create_user(
            'user', 
            'user@gmail.com', 
            'testpassword'
        )

    def login(self):
        self.client.login(username=self.user.username, 
            password='testpassword')

    def login_admin(self):
        self.client.login(username=self.staff_user, password="testpassword")


class SchoolSetup(object):
    def setUp(self):
        self.city = CityFactory.create()
        self.school = SchoolFactory.create(city=self.city)


class CompanySetup(object):
    def setUp(self):
        User = get_user_model()

        UserSetup.setUp(self)
        SchoolSetup.setUp(self)
        self.company = CompanyFactory.create(default_school=self.school)

        self.real_estate_user = User.objects.create_user(
            'real_estate_user', 
            're@gmail.com', 
            'testpassword')
        self.real_estate_user.real_estate_company = self.company
        self.real_estate_user.save()
    
    def login_re_user(self):
        # log in a real estate user
        self.client.login(username=self.real_estate_user.username, 
            password='testpassword')


