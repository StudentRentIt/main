from django.contrib.auth import get_user_model
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from .models import Company
from .urls import prefix
from school.models import School
from main.models import City
from test.tests import CompanySetup, UserSetup


class RealEstateSetUp(TestCase):
    def setUp(self):
        CompanySetup.setUp(self)
        
        self.access_denied_message = "You do not have access"


class RealEstateModelTest(RealEstateSetUp):
    def test_company(self):
        Company.objects.get(name=self.company.name)


class RealEstateViewTest(RealEstateSetUp):
    def test_home(self):
        url = reverse(prefix + 'home')
        anon_response = self.client.get(url)
        self.assertEqual(anon_response.status_code, 200)

        url = reverse(prefix + 'company-home', kwargs={'slug':slugify(self.company.name)})
        
        UserSetup.login(self)
        no_access_response = self.client.get(url)
        self.assertContains(no_access_response, self.access_denied_message)

        CompanySetup.login_re_user(self)
        re_response = self.client.get(url)
        self.assertContains(re_response, self.company.name)

    def test_company_members(self):
        url = reverse(prefix + 'company-members', 
            kwargs={'slug':self.company.slug})
        
        UserSetup.login(self)
        no_access_response = self.client.get(url)
        self.assertContains(no_access_response, self.access_denied_message)

        CompanySetup.login_re_user(self)
        re_response = self.client.get(url)
        self.assertContains(re_response, "Member Administration")

    def test_company_properties(self):
        url = reverse(prefix + 'company-properties', 
            kwargs={'slug':self.company.slug})
        
        UserSetup.login(self)
        no_access_response = self.client.get(url)
        self.assertContains(no_access_response, self.access_denied_message)

        CompanySetup.login_re_user(self)
        re_response = self.client.get(url)
        self.assertContains(re_response, "Property")

    def test_company_support(self):
        url = reverse(prefix + 'company-support', 
            kwargs={'slug':self.company.slug})
        
        UserSetup.login(self)
        no_access_response = self.client.get(url)
        self.assertContains(no_access_response, self.access_denied_message)

        CompanySetup.login_re_user(self)
        re_response = self.client.get(url)
        self.assertContains(re_response, "Support")


class RealEstateFormTest(RealEstateSetUp):
    pass

    


