import unittest

from main.models import City
from school.models import School
from property.models import Amenity
from scrape.models import Source, Apartment, ApartmentImage, ApartmentFloorPlan, \
                            AmenityCrossWalk, ApartmentAmenity


class ApartmentTestCase(unittest.TestCase):

    def setUp(self):
        # get required related models
        city = City.objects.create(name="Scrape Test Town", state="TX")
        school = School.objects.create(city=city, name="Scrape Test University",
                        long=-97.1234123, lat=45.7801234)
        amenity1 = Amenity.objects.create(amenity="test amenity 1", type="CMW")
        amenity2 = Amenity.objects.create(amenity="test amenity 2", type="BIN", special=True)


        # set up the scrape models
        self.source1 = Source.objects.create(name="test source 1", link="www.test1.com")
        self.source2 = Source.objects.create(name="test source 2", link="www.test2.com")

        self.apartment1 = Apartment.objects.create(source=self.source1, school=school,
                            title="test apartment1", address="512 Craddock Ave",
                            lat=29.893543, long=-97.962989, city="San Marcos", state="TX",
                            zip_cd="78666", phone="1231234123", description="Ipsum Lorem blah blah", exists=True)
        self.apartment2 = Apartment.objects.create(source=self.source2, school=school,
                            title="test apartment1", address="950 Colgate College Station, TX 77840",
                            lat=30.617857, long=-96.300724, city="College Station", state="TX",
                            zip_cd="77840", phone="(123)123-1234", description="asdfasfka;sdf;kasdf",
                            exists=False)

        self.apartmentimage1 = ApartmentImage.objects.create(apartment=self.apartment1,
                link="http://a1.res.cloudinary.com/apartmentlist/image/upload/t_r_fp_dream_ldp/fda4c891f87b490e99947b2aa8ec46e4.jpg")
        self.apartmentimage2 = ApartmentImage.objects.create(apartment=self.apartment1,
                link="http://a2.res.cloudinary.com/apartmentlist/image/upload/t_r_fp_dream_ldp/94117d8a840ab3239c40a7ad0ef89cae.jpg")
        self.apartmentimage3 = ApartmentImage.objects.create(apartment=self.apartment2,
                link="http://a2.res.cloudinary.com/apartmentlist/image/upload/t_r_fp_dream_ldp/1d0fc533a1aa6f8fd71d9ace75f9f1bb.jpg")
        self.apartmentimage4 = ApartmentImage.objects.create(apartment=self.apartment2,
                link="http://a4.res.cloudinary.com/apartmentlist/image/upload/t_r_fp_dream_ldp/94431e815de00f92faa30d8c4c138ded.jpg")
        self.apartmentimage5 = ApartmentImage.objects.create(apartment=self.apartment2,
                link="http://a2.res.cloudinary.com/apartmentlist/image/upload/t_r_fp_dream_ldp/aaec6c92ac8f1a457dfea0038a10fdc6.jpg")

        self.apartmentfloorplan1 = ApartmentFloorPlan.objects.create(apartment=self.apartment1, price=570,
                                    bed_count=0, bath_count=1, sq_ft=500)
        self.apartmentfloorplan2 = ApartmentFloorPlan.objects.create(apartment=self.apartment1, price=685,
                                    bed_count=1, bath_count=1.5, sq_ft=650)
        self.apartmentfloorplan3 = ApartmentFloorPlan.objects.create(apartment=self.apartment2, price=1025,
                                    bed_count=3, bath_count=2.5, sq_ft=985)

        self.amenitycrosswalk1 = AmenityCrossWalk.objects.create(amenity=amenity1, scrape_title="amenity 1")
        self.amenitycrosswalk2 = AmenityCrossWalk.objects.create(amenity=amenity2, scrape_title="amenity 2")

        self.apartmentamenity1 = ApartmentAmenity.objects.create(apartment=self.apartment1, title="amenity 1")
        self.apartmentamenity3 = ApartmentAmenity.objects.create(apartment=self.apartment2, title="amenity 1")
        self.apartmentamenity4 = ApartmentAmenity.objects.create(apartment=self.apartment2, title="amenity 2")


    def test_models(self):
        source = Source.objects.get(id=1)
        apartment = Apartment.objects.get(id=1)
