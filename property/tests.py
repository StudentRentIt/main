from django.utils import unittest
from django.contrib.auth.models import User

from main.models import City
from property.models import Property, PropertyLeaseTerm, PropertyLeaseType, PropertyLeaseStart, \
                            Amenity, Service, Package, PropertyImage, PropertyVideo, \
                            PropertyRoom, PropertySchedule, PropertyFavorite, PropertyReserve
from school.models import School


class PropertyTestCase(unittest.TestCase):

    def setUp(self):
        # set up required model instances
        city = City.objects.create(name="Property Test Town", state="TX")
        user = User.objects.create_user('propertytester', 'propertytester@somewhere.com', 'testpassword')
        school = School.objects.create(city=city, name="Property Test University",
                        long=-97.1234123, lat=45.7801234)

        # set up the school models
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

        property = Property.objects.create(school=school, user=user, title="test property",
                        addr="13 Test St.", city="Test Town", state="TX")

        #create many to many objects to property
        image1 = PropertyImage.objects.create(property=property,
                    image_link="http://a2.res.cloudinary.com/apartmentlist/image/upload/t_r_fp_dream_ldp/94117d8a840ab3239c40a7ad0ef89cae.jpg",
                    caption="test caption", floorplan=True)
        image2 = PropertyImage.objects.create(property=property,
                    image_link="http://a1.res.cloudinary.com/apartmentlist/image/upload/t_r_fp_dream_ldp/fda4c891f87b490e99947b2aa8ec46e4.jpg",
                    order=3, main=True)

        video = PropertyVideo.objects.create(property=property, video_link='<iframe width="560" height="315" src="//www.youtube.com/embed/TefqMF2ls1U" frameborder="0" allowfullscreen></iframe>')
        room1 = PropertyRoom.objects.create(property=property, lease_start=lease_start, price=500,
                    bed_count=0, bath_count=1, sq_ft=800)
        room2 = PropertyRoom.objects.create(property=property, lease_start=lease_start, price=900,
                    bed_count=1, bath_count=1.5, sq_ft=920)
        favorite = PropertyFavorite.objects.create(property=property, user=user,
                        note="test property note")
        reserve = PropertyReserve.objects.create(property=property, user=user,
                    first_name="mr", last_name="tester", email="tester@gmail.com",
                    phone_number=123412341, floor_plan=room1, move_in_date="2014-09-01")
        schedule = PropertySchedule.objects.create(property=property, user=user,
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
        property = Property.objects.get(id=1)

        property_room = PropertyRoom.objects.get(id=1)
        property_image = PropertyImage.objects.get(id=1)
        property_video = PropertyVideo.objects.get(id=1)
        property_favorite = PropertyFavorite.objects.get(id=1)
        property_schedule = PropertySchedule.objects.get(id=1)
        property_reserve = PropertyReserve.objects.get(id=1)
