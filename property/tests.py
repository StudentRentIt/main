from django.utils import unittest
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from django_webtest import WebTest

from main.models import City, UserProfile
from main.tests import TestUser
from property.utils import can_edit_property_list
from property.models import Property, PropertyLeaseTerm, PropertyLeaseType, PropertyLeaseStart, \
                            Amenity, Service, Package, PropertyImage, PropertyVideo, \
                            PropertyRoom, PropertySchedule, PropertyFavorite, PropertyReserve
from school.models import School, Deal, Event
from realestate.models import Company


class PropertyTestCase(unittest.TestCase):

    def setUp(self):
        # set up required model instances for properties
        city = City.objects.create(name="Property Test Town", state="TX")
        user = User.objects.create_user('propertytester', 'propertytester@somewhere.com', 'testpassword')
        school = School.objects.create(city=city, name="Property Test University",
                        long=-97.1234123, lat=45.7801234)

        # set up the necessary foreign key models
        amenity1 = Amenity.objects.create(amenity="test amenity 1", type="CMW")
        amenity2 = Amenity.objects.create(amenity="test amenity 2", type="BIN", special=True)
        service1 = Service.objects.create(title="test service 1", description="this is the first test service",
                        price=20)
        service2 = Service.objects.create(title="test service 2", description="this is the second test service",
                        price=50, service_type="O")
        package = Package.objects.create(title="test package", description="this is the test package",
                    price=100)
        package.services.add(service1, service2)

        lease_type = PropertyLeaseType.objects.create(lease_type="test lease type")
        lease_term = PropertyLeaseTerm.objects.create(lease_term="test lease term", order=1)
        lease_start = PropertyLeaseStart.objects.create(lease_start="test lease start", order=1)

        
        # set up real_estate with multiple users that can view the Real Estate info
        real_estate_company = Company.objects.create(name="Test Real Estate")
        real_estate_user = User.objects.create_user(username='realestatetester', email='realestatetester@somewhere.com', 
            password='testpassword', first_name="Real Estate", last_name="Tester" )
        real_estate_user_profile = UserProfile.objects.get(user=real_estate_user)
        real_estate_user_profile.phone_number="5091231234"
        real_estate_user_profile.save()

        self.property = Property.objects.create(school=school, user=user, title="test property",
                        addr="13 Test St.", city="Test Town", state="TX")
        real_estate_property = Property.objects.create(school=school, user=real_estate_user, title="test property with real estate",
                        addr="13 Test St.", city="Test Town", state="TX", real_estate_company=real_estate_company)

        #create many to many objects to property
        image1 = PropertyImage.objects.create(property=self.property,
                    image_link="http://a2.res.cloudinary.com/apartmentlist/image/upload/t_r_fp_dream_ldp/94117d8a840ab3239c40a7ad0ef89cae.jpg",
                    caption="test caption", floorplan=True)
        image2 = PropertyImage.objects.create(property=self.property,
                    image_link="http://a1.res.cloudinary.com/apartmentlist/image/upload/t_r_fp_dream_ldp/fda4c891f87b490e99947b2aa8ec46e4.jpg",
                    order=3, main=True)

        video = PropertyVideo.objects.create(property=self.property, video_link='<iframe width="560" height="315" src="//www.youtube.com/embed/TefqMF2ls1U" frameborder="0" allowfullscreen></iframe>')
        room1 = PropertyRoom.objects.create(property=self.property, lease_start=lease_start, price=500,
                    bed_count=0, bath_count=1, sq_ft=800)
        room2 = PropertyRoom.objects.create(property=self.property, lease_start=lease_start, price=900,
                    bed_count=1, bath_count=1.5, sq_ft=920)
        favorite = PropertyFavorite.objects.create(property=self.property, user=user,
                        note="test property note")
        reserve = PropertyReserve.objects.create(property=self.property, user=user,
                    first_name="mr", last_name="tester", email="tester@gmail.com",
                    phone_number=123412341, floor_plan=room1, move_in_date="2014-09-01")
        schedule = PropertySchedule.objects.create(property=self.property, user=user,
                    first_name="mr", last_name="tester", email="tester@gmail.com",
                    phone_number=123412341, schedule_date="2014-09-01",
                    schedule_time="8:00 am")

    def test_models(self):
        amenity = Amenity.objects.get(id=1)
        service = Service.objects.get(id=1)
        package = Package.objects.get(id=1)
        lease_type = PropertyLeaseType.objects.get(id=1)
        lease_term = PropertyLeaseTerm.objects.get(id=1)
        lease_start = PropertyLeaseStart.objects.get(id=1)
        real_estate_company = Company.objects.get(id=1)
        property = Property.objects.get(id=1)

        property_room = PropertyRoom.objects.get(id=1)
        property_image = PropertyImage.objects.get(id=1)
        property_video = PropertyVideo.objects.get(id=1)
        property_favorite = PropertyFavorite.objects.get(id=1)
        property_schedule = PropertySchedule.objects.get(id=1)
        property_reserve = PropertyReserve.objects.get(id=1)


class ModelTests(unittest.TestCase):

    def setUp(self):
        # set up required model instances
        self.city = City.objects.create(name="School Test Town", state="TX")
        self.user = User.objects.create_user('schooltester', 'schooltester@somewhere.com', 'testpassword')
        self.real_estate_user = User.objects.create_user('Companytester', 'REtester@somewhere.com', 'REpassword')
        self.real_estate_company = Company.objects.create(name="Test Real Estate")

        # set up the school models
        self.school = School.objects.create(city=self.city, name="School Test University",
                        long=-97.1234123, lat=45.7801234)

        # create property, not at top because school is required first
        self.property = Property.objects.create(school=self.school, user=self.user, title="test property",
                        addr="13 Test St.", city="Test Town", state="TX", real_estate_company=self.real_estate_company)

        self.deal = Deal.objects.create(school=self.school, property=self.property, user=self.user,
                        title="test deal", description="This is the deal object created in testing")

        self.event = Event.objects.create(user=self.user, school=self.school, title="test event",
                    description="this is the test event object", location="somewhere yonder")

        self.favorite = PropertyFavorite.objects.create(property=self.property,
                            user=self.user, note="test note")

    def test_models(self):
        School.objects.get(id=1)
        Deal.objects.get(id=1)
        Event.objects.get(id=1)
        Event.objects.get(id=1)


class ViewTests(TestCase):

    def setUp(self):
        self.client = Client()

        ModelTests.setUp(self)

        self.property_pk = self.property.id
        self.property_slug = slugify(self.property.title)
        self.real_estate_property_pk = self.real_estate_company.id
        self.real_estate_property_slug = slugify(self.real_estate_company.name)

    def test_property_community(self):
        url = reverse('property-community', kwargs={'pk':self.property_pk, 'slug':self.property_slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_manage(self):
        url = '/property/manage/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_add(self):
        url = reverse('add-property')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_update_home(self):
        url = '/property/update/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_update_property(self):
        url = reverse('update-property', kwargs={'pk':self.property_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    # TODO: add post request for Update and Add Property

    def test_type_room(self):
        url = reverse('property-type', args=(self.property_pk, 'room', '1'))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_type_image(self):
        url = reverse('property-type', args=(self.property_pk, 'image', '1'))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_type_video(self):
        url = reverse('property-type', args=(self.property_pk, 'video', '1'))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    '''
    TODO: add post request for these 3 deletes

    def test_type_delete_room(self):
        url = reverse('property-type-delete')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_type_delete_image(self):
        url = reverse('property-type-delete')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_type_delete_video(self):
        url = reverse('property-type-delete')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    '''

    def test_action(self):
        url = reverse('property-action', kwargs={'pk':self.property_pk, 'slug':self.property_slug, 'action':'schedule'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # TODO: Post request

    def test_property(self):
        url = reverse('property', kwargs={'pk':self.property_pk, 'slug':self.property_slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_business(self):
        url = reverse('business', kwargs={'pk':self.property_pk, 'slug':self.property_slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    '''
    TODO: permission test for real estate agents. Need to ensure that only a real estate person
    or the creator of a property can edit/view the property
    '''

    def test_favorites(self):
        url = reverse('favorites')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_property_favorite(self):
        url = reverse('favorite-action', args={'delete'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # TODO: Post request

    def test_recurring(self):
        url = reverse('update-property-recurring-services', kwargs={'pk':self.property_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        # TODO: Test form submit

    def test_onetime(self):
        url = reverse('update-property-onetime-services', kwargs={'pk':self.property_pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

        # TODO: Test form submit

    def test_favorite(self):
        url = '/property/favorites/1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


class FunctionTests(WebTest):

    def setUp(self):
        TestUser.setUp(self)
        ModelTests.setUp(self)

        self.real_estate_user.profile.real_estate_company = self.real_estate_company
        self.real_estate_user.profile.save()

    def test_update_without_properties(self):
        user = self.user

        update_page = self.app.get('/property/update/', user=user)

    def test_update_with_properties(self):
        user = self.real_estate_user
        self.assertNotEqual(can_edit_property_list(user), None)

        update_page = self.app.get('/property/update/', user=user) 


    # TODO: test_submit_schedule_form

    # TODO: test_submit_contact_form        
