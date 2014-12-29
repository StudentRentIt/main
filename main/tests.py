from django.contrib.auth import get_user_model
from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from django_webtest import WebTest

from .models import City, Payment, TeamMember, Contact
from school.models import School
from realestate.models import Company
from test.tests import CompanySetup, UserSetup


class MainTestSetup(TestCase):
    def setUp(self):
        CompanySetup.setUp(self)

        self.contact = Contact.objects.create(first_name="Mr", last_name="Tester",
                    email="tester@gmail.com", phone_number=1231231234, subject="Test Subject",
                    body="this is the contact body")

        self.manage_text = 'glyphicon-pencil'
        

class MainModelTests(MainTestSetup):
    def test_models(self):
        City.objects.get(id=1)
        Contact.objects.get(id=1)


class MainViewTests(MainTestSetup):
    def test_home(self):
        url = reverse('home-list')
        manage_url = reverse('manage-property')
        
        anon_response = self.client.get(url)
        self.assertEqual(anon_response.status_code, 200)
        self.assertNotContains(anon_response, self.manage_text)

        UserSetup.login_admin(self)
        admin_response = self.client.get(url)
        self.assertContains(admin_response, self.manage_text)

        CompanySetup.login_re_user(self)
        re_response = self.client.get(url)
        self.assertContains(re_response, "Dashboard")
        self.assertNotContains(re_response, self.manage_text)

    def test_search(self):
        url = reverse('search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_search_school(self):
        url = reverse('search', kwargs={'slug':slugify(self.school.name)})

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # test the post of a blank property search
        post = {
            'priceMin': '', 'priceMax': '', 'leaseType':'', 'leaseTerm':'',
            'leaseStart':'', 'bathMin':'', 'bathMax':'', 'bedMin':'', 'bedMax':'',
            'keyword':''
        }
        response = self.client.post(reverse('search', 
            kwargs={'slug':slugify(self.school.name)}), post)
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        url = reverse('contact-view')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_school_list(self):
        url = reverse('school-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_property_list(self):
        url = reverse('property-list', kwargs={'pk':'1'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_profile(self):
        url = reverse('user_profile')
        UserSetup.login(self)

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Update Profile")

    def test_mongoose(self):
        url = reverse('mongoose-analytics')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_how_it_works(self):
        url = reverse('how-it-works')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        url = '/about/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_privacy(self):
        url = '/privacy/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_terms(self):
        url = '/terms/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_payment(self):
        url = reverse('payment')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

