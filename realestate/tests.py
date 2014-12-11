from django.utils import unittest
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate
from django.utils.text import slugify

from realestate.models import Company
from school.models import School
from main.models import City


class ModelTests(unittest.TestCase):

    def setUp(self):
        # set up required model instances
        self.city = City.objects.create(name="School Test Town", state="TX")
        self.school = School.objects.create(city=self.city, name="RE Test University",
                        long=-97.1234123, lat=45.7801234)
        self.company = Company.objects.create(name="Test Company", default_school=self.school)
        
    def test_models(self):
        Company.objects.get(id=1)


class ViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user('retester', 'retester@somewhere.com', 'testpassword')
        self.client = Client()

        # set up models
        ModelTests.setUp(self)


    def test_home(self):
        url = reverse('re-home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_company(self):
        url = reverse('re-company', kwargs={'slug':slugify(self.company.name)})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

