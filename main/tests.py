from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from django_webtest import WebTest

from test.factories import CityFactory, SchoolFactory, CompanyFactory, RealEstateUserFactory, \
                           NormalUserFactory, ContactFactory, StaffUserFactory

class MainTestSetup(TestCase):
    def setUp(self):
        self.user = NormalUserFactory.create()
        self.staff_user = StaffUserFactory.create()
        self.city = CityFactory.create()
        self.school = SchoolFactory.create(city=self.city)
        self.company = CompanyFactory.create(default_school=self.school)
        self.real_estate_user = RealEstateUserFactory.create(real_estate_company=self.company)
        self.contact = ContactFactory.create()

        self.manage_text = 'glyphicon-pencil'


class MainViewTests(MainTestSetup, WebTest):
    csrf_checks = False

    def test_home(self):
        url = reverse('home-list')
        
        anon_response = self.app.get(url)
        self.assertNotContains(anon_response, self.manage_text)

        admin_response = self.app.get(url, user=self.staff_user)
        self.assertContains(admin_response, self.manage_text)

        re_response = self.app.get(url, user=self.real_estate_user)
        self.assertContains(re_response, "Dashboard")
        self.assertNotContains(re_response, self.manage_text)

    def test_search(self):
        url = reverse('search')
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    def test_search_school(self):
        url = reverse('search', kwargs={'slug':slugify(self.school.name)})

        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

        # test the post of a blank property search
        post = {
            'priceMin': '', 'priceMax': '', 'leaseType':'', 'leaseTerm':'',
            'leaseStart':'', 'bathMin':'', 'bathMax':'', 'bedMin':'', 'bedMax':'',
            'keyword':''
        }
        response = self.app.post(reverse('search', 
            kwargs={'slug':slugify(self.school.name)}), post)
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        url = reverse('contact-view')
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    def test_school_list(self):
        url = reverse('school-list')
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    def test_property_list(self):
        url = reverse('property-list', kwargs={'pk':'1'})
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_profile(self):
        url = reverse('user_profile')
        response = self.app.get(url, user=self.user)
        self.assertContains(response, "Update Profile")

    def test_mongoose(self):
        url = reverse('mongoose-analytics')
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    def test_how_it_works(self):
        url = reverse('how-it-works')
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        url = '/about/'
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    def test_privacy(self):
        url = '/privacy/'
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    def test_terms(self):
        url = '/terms/'
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    def test_payment(self):
        url = reverse('payment')
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

