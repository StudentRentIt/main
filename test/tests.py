from django.contrib.auth import get_user_model
from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from main.models import City, Payment, TeamMember, Contact
from school.models import School, Deal, Event
from realestate.models import Company
from property.models import Property, PropertyFavorite


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
        self.city = City.objects.create(name="Test Town", state="TX")
        self.school = School.objects.create(city=self.city, name="RE Test University",
                        long=-97.1234123, lat=45.7801234)


class CompanySetup(object):
    def setUp(self):
        User = get_user_model()

        UserSetup.setUp(self)
        SchoolSetup.setUp(self)
        self.company = Company.objects.create(name="Test Company", default_school=self.school)

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


class PropertySetup(object):
    def setUp(self):
        User = get_user_model()
        CompanySetup.setUp(self)

        

        # create property, not at top because school is required first
        self.property = Property.objects.create(school=self.school, user=self.user, title="test property",
                        addr="13 Test St.", city="Test Town", state="TX", real_estate_company=self.company)

        self.deal = Deal.objects.create(school=self.school, property=self.property, user=self.user,
                        title="test deal", description="This is the deal object created in testing")

        self.event = Event.objects.create(user=self.user, school=self.school, title="test event",
                    description="this is the test event object", location="somewhere yonder")

        self.favorite = PropertyFavorite.objects.create(property=self.property,
                            user=self.user, note="test note")


