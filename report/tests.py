from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from report.views import admin_home
from test.tests import CompanySetup, UserSetup

'''
The report app gives the project a way to keep reports organized, easily 
maintainable and expandable. There are different sections for different 
user groups that will be able to see different reports, or shared reports
with different data sets based on permissions.
'''

class ReportTestSetup(TestCase):
    def setUp(self):
        CompanySetup.setUp(self)


class ViewTests(ReportTestSetup):
    def test_admin_home(self):
        '''
        TODO: test with anon users. @staff_member_required gives status of 200
        so we can't use normal method
        '''
        UserSetup.login_admin(self)
        response = self.client.get(reverse('report-admin-home'))
        self.assertEqual(response.status_code, 200)

    def test_business_home(self):
        anon_response = self.client.get(reverse('report-business-home'))
        self.assertEqual(anon_response.status_code, 302)

        UserSetup.login_admin(self)
        response = self.client.get(reverse('report-business-home'))
        self.assertEqual(response.status_code, 200)

    def test_real_estate_home(self):
        anon_response = self.client.get(reverse('report-real-estate-home'))
        self.assertEqual(anon_response.status_code, 302)

        CompanySetup.login_re_user(self)
        re_response = self.client.get(reverse('report-real-estate-home'))
        self.assertEqual(re_response.status_code, 200)



