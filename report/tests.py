from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from report.views import admin_home
from main.tests import MainTestSetup

from django_webtest import WebTest

'''
The report app gives the project a way to keep reports organized, easily 
maintainable and expandable. There are different sections for different 
user groups that will be able to see different reports, or shared reports
with different data sets based on permissions.
'''

class ReportTestSetup(MainTestSetup):
    def setUp(self):
        MainTestSetup.setUp(self)


class ViewTests(ReportTestSetup):
	def test_admin_home(self):
		'''
		TODO: test with anon users. @staff_member_required gives status of 200
		so we can't use normal method
		'''
		self.client.login(username="staff_user", password="testpassword")
		response = self.client.get(reverse('report-admin-home'))
		self.assertEqual(response.status_code, 200)

	def test_business_home(self):
		anon_response = self.client.get(reverse('report-business-home'))
		self.assertEqual(anon_response.status_code, 302)

		self.login_admin()
		response = self.client.get(reverse('report-business-home'))
		self.assertEqual(response.status_code, 200)

	def test_real_estate_home(self):
		anon_response = self.client.get(reverse('report-real-estate-home'))
		self.assertEqual(anon_response.status_code, 302)

		self.login_re_user()
		re_response = self.client.get(reverse('report-real-estate-home'))
		self.assertEqual(re_response.status_code, 200)



