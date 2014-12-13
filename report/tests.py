from django.test import TestCase, Client
from django.core.urlresolvers import reverse

'''
The report app gives the project a way to keep reports organized, easily 
maintainable and expandable. There are different sections for different 
user groups that will be able to see different reports, or shared reports
with different data sets based on permissions.
'''

class ViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_admin_home(self):
        url = reverse('report-admin-home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_business_home(self):
        url = reverse('report-business-home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_real_estate_home(self):
        url = reverse('report-real-estate-home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)