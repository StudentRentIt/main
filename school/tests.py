from django.utils import unittest
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.test import Client, TestCase

from main.models import City
from property.models import Property
from school.models import School, Deal, Event, Roommate


class ModelTests(unittest.TestCase):

    def setUp(self):
        # set up required model instances
        self.city = City.objects.create(name="School Test Town", state="TX")
        self.user = User.objects.create_user('schooltester2', 'schooltester@somewhere.com', 'testpassword')

        # set up the school models
        self.school = School.objects.create(city=self.city, name="School Test University",
                        long=-97.1234123, lat=45.7801234)

        # create property, not at top because school is required first
        self.property = Property.objects.create(school=self.school, user=self.user, title="test property",
                        addr="13 Test St.", city="Test Town", state="TX")

        self.deal = Deal.objects.create(school=self.school, property=self.property, user=self.user,
                        title="test deal", description="This is the deal object created in testing")

        self.event = Event.objects.create(user=self.user, school=self.school, title="test event",
                    description="this is the test event object", location="somewhere yonder")

        self.roomate = Roommate.objects.create(user=self.user, school=self.school, property=self.property,
                        name="Billy", message="Looking for you!")

    def test_models(self):
        School.objects.get(id=1)
        Deal.objects.get(id=1)
        Event.objects.get(id=1)
        Event.objects.get(id=1)


class ViewTests(TestCase):

    def setUp(self):
        self.client = Client()

        ModelTests.setUp(self)

        self.school_pk = self.school.id
        self.school_slug = slugify(self.school.name)

    def test_school_articles(self):
        url = reverse('school-articles', kwargs={'pk':self.school_pk, 'slug':self.school_slug, 'type':'articles'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # TODO: Test form submit

    def test_school_events(self):
        url = reverse('school-events', kwargs={'pk':self.school_pk, 'slug':self.school_slug, 'type':'events'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # TODO: Test form submit

    def test_school_deals(self):
        url = reverse('school-deals', kwargs={'pk':self.school_pk, 'slug':self.school_slug, 'type':'deals'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # TODO: Test form submit

    def test_school_roommates(self):
        url = reverse('school-roommates', kwargs={'pk':self.school_pk, 'slug':self.school_slug, 'type':'roommates'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # TODO: Test form submit

    def test_school_article(self):
        url = reverse('update-article', kwargs={'pk':'1'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_school_event(self):
        url = reverse('update-event', kwargs={'pk':'1'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_school_deal(self):
        url = reverse('update-deal', kwargs={'pk':'1'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_school_roommate(self):
        url = reverse('update-roommate', kwargs={'pk':'1'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_school_update_articles(self):
        url = reverse('update-articles')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        # TODO: add post

    def test_school_update_events(self):
        url = reverse('update-events')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        # TODO: add post

    def test_school_update_deals(self):
        url = reverse('update-deals')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        # TODO: add post

    def test_school_update_roommates(self):
        url = reverse('update-roommates')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        # TODO: add post

    def test_school_home(self):
        url = '/school/1/test-school/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 301)
