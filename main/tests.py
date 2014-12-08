from django.utils import unittest
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate

from main.models import City, UserProfile, Payment, TeamMember, Contact
from school.models import School

from django_webtest import WebTest
from django_dynamic_fixture import G

class TestUser(WebTest):

    def setUp(self):
        self.staff = G(User, is_staff=True)
        self.customer = G(User, username='10000', is_staff=False)

    def test_footer_search(self):
        '''
        have the user run a search for a school in the footer and that search should bring us to the results of
        the school search
        '''
        
        # pull up the home page
        home_page = self.app.get(reverse('home-list'), user=self.customer)

        # search for a school
        form = home_page.forms['search-footer']
        form['search-footer-text'] = "University of Washington"
        form.submit()


class ModelTests(unittest.TestCase):

    def setUp(self):
        # set up required model instances
        self.user = User.objects.create_user('maintester', 'maintester@somewhere.com', 'testpassword')

        # set up the main models
        self.city = City.objects.create(name="Test Town", state="TX")
        self.payment = Payment.objects.create(user=self.user, amount=500)
        self.team_member = TeamMember.objects.create(user=self.user, name="Bob", title="Tester")
        self.contact = Contact.objects.create(first_name="Mr", last_name="Tester",
                    email="tester@gmail.com", phone_number=1231231234, subject="Test Subject",
                    body="this is the contact body")

    def test_models(self):
        UserProfile.objects.get(id=1)
        City.objects.get(id=1)
        Payment.objects.get(id=1)
        TeamMember.objects.get(id=1)
        Contact.objects.get(id=1)


class ViewTests(TestCase):

    def setUp(self):
        self.client = Client()

        # instance setup
        self.user = User.objects.create_user('maintester', 'maintester@somewhere.com', 'testpassword')
        self.city = City.objects.create(name="Test Town", state="TX")
        self.school = School.objects.create(city=self.city, name="School Test University",
                    long=-97.1234123, lat=45.7801234)

    def test_home(self):
        url = reverse('home-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_search(self):
        url = reverse('search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_search_school(self):
        url = reverse('search', kwargs={'slug':'school-test-university'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # test the post of a blank property search
        response = self.client.post(reverse('search', kwargs={'slug':'school-test-university'}),
            {'priceMin': '', 'priceMax': '', 'leaseType':'', 'leaseTerm':'',
            'leaseStart':'', 'bathMin':'', 'bathMax':'', 'bedMin':'', 'bedMax':'',
            'keyword':''})
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
        authenticate(username=self.user.username, password=self.user.password)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

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

