from django.test import TestCase
from django.core.urlresolvers import reverse

from django_webtest import WebTest

from .models import Company
from .urls import prefix
from test.factories import CityFactory, SchoolFactory, CompanyFactory, RealEstateUserFactory, \
                           NormalUserFactory
from test.tests import AccessMixin
                           

class RealEstateSetUp(object):
    def setUp(self):
        self.user = NormalUserFactory.create()
        self.city = CityFactory.create()
        self.school = SchoolFactory.create(city=self.city)
        self.company = CompanyFactory.create(default_school=self.school)
        self.real_estate_user = RealEstateUserFactory.create(real_estate_company=self.company)

        self.access_denied_message = "You do not have access"


class RealEstateModelTest(RealEstateSetUp):
    def test_random_contact(self):
        contact = self.company.get_random_contact()
        
        self.assertEqual(contact, self.real_estate_user)
        self.assertNotEqual(contact, self.user)


class RealEstateViewTest(AccessMixin, RealEstateSetUp, WebTest):
    def test_home(self):
        url = reverse(prefix + 'home')
        anon_response = self.app.get(url)
        self.assertEqual(anon_response.status_code, 200)

    def test_company_home(self):
        url = self.company.get_absolute_url()
        self.real_estate_access(url, self.company.name)

    def test_company_members(self):
        url = reverse(prefix + 'company-members', 
            kwargs={'slug':self.company.slug})
        self.real_estate_access(url, "Member Administration")

    def test_company_properties(self):
        url = reverse(prefix + 'company-properties', 
            kwargs={'slug':self.company.slug})
        self.real_estate_access(url, "Property")

    def test_company_support(self):
        url = reverse(prefix + 'company-support', 
            kwargs={'slug':self.company.slug})
        self.real_estate_access(url, "Support")
    


