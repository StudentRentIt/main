from django.test import TestCase
from django.core.urlresolvers import reverse

from django_webtest import WebTest

from test.factories import CityFactory, SchoolFactory, CompanyFactory, RealEstateUserFactory, \
                           NormalUserFactory, StaffUserFactory
from test.tests import AccessMixin

'''
The report app gives the project a way to keep reports organized, easily 
maintainable and expandable. There are different sections for different 
user groups that will be able to see different reports, or shared reports
with different data sets based on permissions.
'''

class ReportTestSetup(TestCase):
    def setUp(self):
        self.user = NormalUserFactory.create()
        self.staff_user = StaffUserFactory.create()
        self.city = CityFactory.create()
        self.school = SchoolFactory.create(city=self.city)
        self.company = CompanyFactory.create(default_school=self.school)
        self.real_estate_user = RealEstateUserFactory.create(real_estate_company=self.company)


class ViewTests(AccessMixin, ReportTestSetup, WebTest):
    def test_admin_home(self):
        url = reverse('report-admin-home')
        self.staff_required(url, "Admin Dashboard")

    def test_business_home(self):
        url = reverse('report-business-home')
        self.staff_required(url, "Business Dashboard")

    def test_real_estate_home(self):
        url = reverse('report-real-estate-home')
        self.staff_required(url, "Real Estate")



