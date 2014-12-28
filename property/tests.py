from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from .models import Property, PropertyLeaseTerm, PropertyLeaseType, PropertyLeaseStart, \
                            Amenity, PropertyImage, PropertyVideo, PropertyRoom, \
                            PropertySchedule, PropertyFavorite, PropertyReserve
from school.models import Deal, Event
from test.tests import UserSetup, PropertySetup


class PropertySetUp(TestCase):
    def setUp(self):
        PropertySetup.setUp(self)

        self.property_slug = slugify(self.property.title)


class PropertyModelTests(PropertySetUp):
    def test_property(self):
        Property.objects.get(id=1)

    def test_deal(self):
        Deal.objects.get(id=1)

    def test_event(self):
        Event.objects.get(id=1)


class PropertyViewTests(PropertySetUp):
    def test_property_community(self):
        url = reverse('property-community', kwargs={'pk':self.property.id, 'slug':self.property_slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_manage(self):
        url = '/property/manage/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_add(self):
        url = reverse('add-property')
        anon_response = self.client.get(url)
        self.assertEqual(anon_response.status_code, 302)

        UserSetup.login_admin(self)
        admin_response = self.client.get(url)
        self.assertEqual(admin_response.status_code, 200)

    def test_update_home(self):
        url = '/property/update/'
        anon_response = self.client.get(url)
        self.assertEqual(anon_response.status_code, 302)

        UserSetup.login_admin(self)
        admin_response = self.client.get(url)
        self.assertEqual(admin_response.status_code, 200)

    def test_update_property(self):
        url = reverse('update-property', kwargs={'pk':self.property.id})
        anon_response = self.client.get(url)
        self.assertEqual(anon_response.status_code, 302)

        UserSetup.login_admin(self)
        admin_response = self.client.get(url)
        self.assertEqual(admin_response.status_code, 200)

    def test_type_room(self):
        url = reverse('property-type', args=(self.property.id, 'room', '1'))
        anon_response = self.client.get(url)
        self.assertEqual(anon_response.status_code, 302)

        UserSetup.login_admin(self)
        admin_response = self.client.get(url)
        self.assertEqual(admin_response.status_code, 200)

    def test_type_image(self):
        url = reverse('property-type', args=(self.property.id, 'image', '1'))
        anon_response = self.client.get(url)
        self.assertEqual(anon_response.status_code, 302)

        UserSetup.login_admin(self)
        admin_response = self.client.get(url)
        self.assertEqual(admin_response.status_code, 200)

    def test_type_video(self):
        url = reverse('property-type', args=(self.property.id, 'video', '1'))
        anon_response = self.client.get(url)
        self.assertEqual(anon_response.status_code, 302)

        UserSetup.login_admin(self)
        admin_response = self.client.get(url)
        self.assertEqual(admin_response.status_code, 200)

    def test_action(self):
        url = reverse('property-action', kwargs={
            'pk':self.property.id, 
            'slug':self.property_slug, 
            'action':'schedule'
        })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_property(self):
        url = reverse('property', kwargs={'pk':self.property.id, 'slug':self.property_slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_business(self):
        url = reverse('business', kwargs={'pk':self.property.id, 'slug':self.property_slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_favorites(self):
        url = reverse('favorites')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_property_favorite(self):
        url = reverse('favorite-action', args={'delete'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # TODO: Post request

    def test_favorite(self):
        url = '/property/favorites/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        UserSetup.login(self)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
