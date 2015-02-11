from django.core.urlresolvers import reverse
from django.test import Client, TestCase
from django.utils.text import slugify

from django_webtest import WebTest

from .models import Property, PropertyLeaseTerm, PropertyLeaseType, PropertyLeaseStart, \
                            Amenity, PropertyImage, PropertyVideo, PropertyRoom, \
                            PropertySchedule, PropertyFavorite, PropertyReserve
from school.models import Deal, Event
from test.factories import *
from test.tests import AccessMixin


class PropertySetUp(TestCase):
    def setUp(self):
        self.user = NormalUserFactory.create()
        self.staff_user = StaffUserFactory.create()
        self.city = CityFactory.create()
        self.school = SchoolFactory.create(city=self.city)
        self.company = CompanyFactory.create(default_school=self.school)
        self.real_estate_user = RealEstateUserFactory.create(real_estate_company=self.company)
        self.property = PropertyFactory.create(school=self.school, user=self.user, 
            real_estate_company=self.company)
        self.deal = DealFactory.create(school=self.school, property=self.property, user=self.user)
        self.event = EventFactory.create(user=self.user, school=self.school)
        self.favorite = FavoriteFactory.create(property=self.property, user=self.user)

        self.property_slug = slugify(self.property.title)


class PropertyModelTests(PropertySetUp):
    def test_get_contact(self):
        contact = self.property.get_contact_user()

        self.assertEqual(contact, self.real_estate_user)
        self.assertNotEqual(contact, self.user)


class PropertyViewTests(AccessMixin, PropertySetUp, WebTest):
    def test_property_community(self):
        url = reverse('property-community', 
            kwargs={'pk':self.property.id, 'slug':self.property_slug})
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    def test_manage(self):
        url = reverse('manage-property')
        response = self.app.get(url)
        self.assertEqual(response.status_code, 302)

    def test_add(self):
        url = reverse('add-property')
        self.staff_required(url)

    def test_update_home(self):
        url = '/property/update/'
        self.staff_required(url)

    def test_update_property(self):
        url = reverse('update-property', kwargs={'pk':self.property.id})
        self.staff_required(url)

    def test_property(self):
        url = reverse('property', kwargs={'pk':self.property.id, 'slug':self.property_slug})
        response = self.app.get(url)

        assert self.property.title in response
        assert self.real_estate_user.first_name in response
        assert self.company.phone in response

    def test_property_contact(self):
        url = reverse('property-action', kwargs={
            'pk':self.property.id, 
            'slug':self.property_slug,
            'action':'contact'
        })
        response = self.app.get(url)
        assert "Contact Agent" in response

    def test_business(self):
        url = reverse('business', kwargs={'pk':self.property.id, 'slug':self.property_slug})
        response = self.app.get(url)
        assert self.property.title in response

    def test_favorites(self):
        url = reverse('favorites')
        response = self.app.get(url)
        self.assertEqual(response.status_code, 302)

    def test_property_favorite(self):
        url = reverse('favorite-action', args={'delete'})
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    def test_favorite(self):
        url = self.favorite.get_absolute_url()
        self.login_required(url)


# PropertyFormTest(PropertySetUp, WebTest):
#     def test_action(self):
#         url = reverse('property-action', kwargs={
#             'pk':self.property.id, 
#             'slug':self.property_slug, 
#             'action':'schedule'
#         })
#         response = self.app.get(url)
#         self.assertEqual(response.status_code, 200)
