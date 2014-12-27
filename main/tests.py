from django.contrib.auth import get_user_model
from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from django_webtest import WebTest

from .models import City, UserProfile, Payment, TeamMember, Contact
from school.models import School
from realestate.models import Company


class MainTestSetup(TestCase):
    def setUp(self):
        User = get_user_model()

        # set up all types of users to be used
        self.staff_user = User.objects.create_user('staff_user', 'staff@gmail.com', 'testpassword')
        self.staff_user.is_staff = True
        self.staff_user.save()

        self.user = User.objects.create_user('user', 'user@gmail.com', 'testpassword')
        
        self.city = City.objects.create(name="Test Town", state="TX")
        self.school = School.objects.create(city=self.city, name="RE Test University",
                        long=-97.1234123, lat=45.7801234)
        self.company = Company.objects.create(name="Test Company", default_school=self.school)
        self.payment = Payment.objects.create(user=self.user, amount=500)
        self.team_member = TeamMember.objects.create(user=self.user, name="Bob", title="Tester")
        self.contact = Contact.objects.create(first_name="Mr", last_name="Tester",
                    email="tester@gmail.com", phone_number=1231231234, subject="Test Subject",
                    body="this is the contact body")

        self.real_estate_user = User.objects.create_user(
            'real_estate_user', 're@gmail.com', 'testpassword')
        self.real_estate_user.profile.real_estate_company = self.company
        self.real_estate_user.profile.save()

        self.manage_text = 'glyphicon-pencil'

    def login(self):
        self.client.login(username=self.user.username, 
            password='testpassword')

    def login_re_user(self):
        # log in a real estate user
        self.client.login(username=self.real_estate_user.username, 
            password='testpassword')

    def login_admin(self):
        self.client.login(username=self.staff_user, password="testpassword")
        

class MainModelTests(MainTestSetup):
    def test_models(self):
        UserProfile.objects.get(id=1)
        City.objects.get(id=1)
        Payment.objects.get(id=1)
        TeamMember.objects.get(id=1)
        Contact.objects.get(id=1)


class MainViewTests(MainTestSetup):
    def test_home(self):
        url = reverse('home-list')
        manage_url = reverse('manage-property')
        
        anon_response = self.client.get(url)
        self.assertEqual(anon_response.status_code, 200)
        self.assertNotContains(anon_response, self.manage_text)

        self.login_admin()
        admin_response = self.client.get(url)
        self.assertContains(admin_response, self.manage_text)

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
        self.login()

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

