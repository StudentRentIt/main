from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from main.tests import TestUser
from report.views import admin_home

from django_webtest import WebTest

'''
The report app gives the project a way to keep reports organized, easily 
maintainable and expandable. There are different sections for different 
user groups that will be able to see different reports, or shared reports
with different data sets based on permissions.
'''


class ViewTests(TestCase):

	def setUp(self):
		TestUser.setUp(self)
		self.client = Client()
		
	def test_admin_home(self):
		'''
		TODO: test with anon users. @staff_member_required gives status of 200
		so we can't use normal method
		'''
		self.client.login(username="staff_user", password="staffpass")
		response = self.client.get(reverse('report-admin-home'))
		self.assertEqual(response.status_code, 200)

	def test_business_home(self):
		anon_response = self.client.get(reverse('report-business-home'))
		self.assertEqual(anon_response.status_code, 302)

		self.client.login(username="user", password="userpass")
		response = self.client.get(reverse('report-business-home'))
		self.assertEqual(response.status_code, 200)

	def test_real_estate_home(self):
		anon_response = self.client.get(reverse('report-real-estate-home'))
		self.assertEqual(anon_response.status_code, 302)

		self.client.login(username="real_estate_user", password="repass")
		re_response = self.client.get(reverse('report-real-estate-home'))
		self.assertEqual(re_response.status_code, 200)



