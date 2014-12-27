from django.contrib.auth.models import User
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from .models import Company
from .urls import prefix
from school.models import School
from main.models import City


class RealEstateSetUp(TestCase):
    def setUp(self):
        # set up required model instances
        self.user = User.objects.create_user(
            'anonretester', 
            'retester@somewhere.com', 
            'testpassword'
        )
        self.real_estate_user = User.objects.create_user(
            'retester', 
            'retester@somewhere.com', 
            'testpassword'
        )
        self.city = City.objects.create(name="School Test Town", state="TX")
        self.school = School.objects.create(city=self.city, name="RE Test University",
                        long=-97.1234123, lat=45.7801234)
        self.company = Company.objects.create(name="Test Company", default_school=self.school)

        self.real_estate_user.profile.real_estate_company = self.company
        self.real_estate_user.profile.save()
        self.access_denied_message = "You do not have access"

    def login(self):
        self.client.login(username=self.user.username, 
            password='testpassword')

    def login_re_user(self):
        '''
        log in a real estate user
        '''
        self.client.login(username=self.real_estate_user.username, 
            password='testpassword')


class RealEstateModelTest(RealEstateSetUp):
    def test_company(self):
        Company.objects.get(name=self.company.name)


class RealEstateViewTest(RealEstateSetUp):
    def test_home(self):
        url = reverse(prefix + 'home')
        anon_response = self.client.get(url)
        self.assertEqual(anon_response.status_code, 200)

    def test_company_home(self):
        url = reverse(prefix + 'company-home', kwargs={'slug':slugify(self.company.name)})
        
        self.login()
        no_access_response = self.client.get(url)
        self.assertContains(no_access_response, self.access_denied_message)

        self.login_re_user()
        re_response = self.client.get(url)
        self.assertContains(re_response, self.company.name)

    def test_company_members(self):
        url = reverse(prefix + 'company-members', kwargs={'slug':slugify(self.company.name)})
        
        self.login()
        no_access_response = self.client.get(url)
        self.assertContains(no_access_response, self.access_denied_message)

        self.login_re_user()
        re_response = self.client.get(url)
        self.assertContains(re_response, "Member Administration")


class RealEstateFormTest(RealEstateSetUp):
    pass

    


