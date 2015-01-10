from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import Client, TestCase
from django.utils.text import slugify

from django_webtest import WebTest

from .models import Property, PropertyLeaseTerm, PropertyLeaseType, PropertyLeaseStart, \
                            Amenity, PropertyImage, PropertyVideo, PropertyRoom, \
                            PropertySchedule, PropertyFavorite, PropertyReserve
from school.models import Deal, Event
from test.factories import *

User = get_user_model()


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

    def test_deal(self):
        Deal.objects.get(id=1)

    def test_event(self):
        Event.objects.get(id=1)


class PropertyViewTests(PropertySetUp, WebTest):
    def test_property_community(self):
        url = reverse('property-community', kwargs={'pk':self.property.id, 'slug':self.property_slug})
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    def test_manage(self):
        url = '/property/manage/'
        response = self.app.get(url)
        self.assertEqual(response.status_code, 302)

    def test_add(self):
        url = reverse('add-property')
        anon_response = self.app.get(url)
        self.assertEqual(anon_response.status_code, 302)
        
        admin_response = self.app.get(url, user=self.staff_user)
        self.assertEqual(admin_response.status_code, 200)

    def test_update_home(self):
        url = '/property/update/'
        anon_response = self.app.get(url)
        self.assertEqual(anon_response.status_code, 302)

        admin_response = self.app.get(url, user=self.staff_user)
        self.assertEqual(admin_response.status_code, 200)

    def test_update_property(self):
        url = reverse('update-property', kwargs={'pk':self.property.id})
        anon_response = self.app.get(url)
        self.assertEqual(anon_response.status_code, 302)

        admin_response = self.app.get(url, user=self.staff_user)
        self.assertEqual(admin_response.status_code, 200)

    def test_type_room(self):
        url = reverse('property-type', args=(self.property.id, 'room', '1'))
        anon_response = self.app.get(url)
        self.assertEqual(anon_response.status_code, 302)

        admin_response = self.app.get(url, user=self.staff_user)
        self.assertEqual(admin_response.status_code, 200)

    def test_type_image(self):
        url = reverse('property-type', args=(self.property.id, 'image', '1'))
        anon_response = self.app.get(url)
        self.assertEqual(anon_response.status_code, 302)

        admin_response = self.app.get(url, user=self.staff_user)
        self.assertEqual(admin_response.status_code, 200)

    def test_type_video(self):
        url = reverse('property-type', args=(self.property.id, 'video', '1'))
        anon_response = self.app.get(url)
        self.assertEqual(anon_response.status_code, 302)

        admin_response = self.app.get(url, user=self.staff_user)
        self.assertEqual(admin_response.status_code, 200)

    def test_action(self):
        url = reverse('property-action', kwargs={
            'pk':self.property.id, 
            'slug':self.property_slug, 
            'action':'schedule'
        })
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    def test_property(self):
        url = reverse('property', kwargs={'pk':self.property.id, 'slug':self.property_slug})
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    def test_business(self):
        url = reverse('business', kwargs={'pk':self.property.id, 'slug':self.property_slug})
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    def test_favorites(self):
        url = reverse('favorites')
        response = self.app.get(url)
        self.assertEqual(response.status_code, 302)

    def test_property_favorite(self):
        url = reverse('favorite-action', args={'delete'})
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

        # TODO: Post request

    def test_favorite(self):
        url = '/property/favorites/1/'
        response = self.app.get(url)
        self.assertEqual(response.status_code, 302)

        response = self.app.get(url, user=self.user)
        self.assertEqual(response.status_code, 200)
