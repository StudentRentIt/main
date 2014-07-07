from django.utils import unittest
from django.contrib.auth.models import User

from main.models import City
from property.models import Property
from school.models import School, Deal, Event, Roommate


class SchoolTestCase(unittest.TestCase):

    def setUp(self):
        # set up required model instances
        city = City.objects.create(name="School Test Town", state="TX")
        user = User.objects.create_user('schooltester', 'schooltester@somewhere.com', 'testpassword')

        # set up the school models
        school = School.objects.create(city=city, name="School Test University",
                        long=-97.1234123, lat=45.7801234)

        # create property, not at top because school is required first
        property = Property.objects.create(school=school, user=user, title="test property",
                        addr="13 Test St.", city="Test Town", state="TX")

        deal = Deal.objects.create(school=school, property=property, user=user,
                        title="test deal", description="This is the deal object created in testing")

        event = Event.objects.create(user=user, school=school, title="test event",
                    description="this is the test event object", location="somewhere yonder")

        roomate = Roommate.objects.create(user=user, school=school, property=property,
                        name="Billy", message="Looking for you!")

    def test_models(self):
        school = School.objects.get(id=1)
        deal = Deal.objects.get(id=1)
        event = Event.objects.get(id=1)
        roommate = Event.objects.get(id=1)
