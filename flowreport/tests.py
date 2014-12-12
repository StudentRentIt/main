# from django.contrib.auth.models import User
# from django.test import Client, TestCase
# from django.core.urlresolvers import reverse
# from django.contrib.auth import authenticate

# from main.models import City, UserProfile, Payment, TeamMember, Contact
# from school.models import School
# from property.tests import PropertyTestCase

# from django_webtest import WebTest

# from django_webtest import WebTest


# class ModelTests(TestCase):
#	No model tests needed


# class ViewTests(WebTest):

# 	def setUp(self):
# 		# set up property data
# 		PropertyTestCase.setUp(self)

# 	def test_home(self):
# 		url = reverse('report-home')
# 		response = self.client.get(url)
# 		self.assertEqual(response.status_code, 302)

	# def test_property_report(self):
	# 	url = reverse('report-prop-detail', kwargs={"pk":self.property.id})
	# 	response = self.client.get(url)
	# 	self.assertEqual(response.status_code, 200)

# class FunctionTests(WebTest):
#	TODO: add functional tests

