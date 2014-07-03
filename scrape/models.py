from datetime import datetime

from django.db import models

from main.models import City
from school.models import School
from property.models import BATH_CHOICES, BED_CHOICES, Amenity

from localflavor.us.models import PhoneNumberField


FEATURE_CHOICES = (
    ('U', 'Unit'),
    ('C', 'Community'),
    ('U', 'Utility'),
)
SCRAPE_STATUS_CHOICES = (
    ('S', 'Success'),
    ('E', 'Error'),
)
SOURCE_CHOICES = (
    ('A', 'apartmentlist.com'),
)


class Source(models.Model):
    name = models.CharField(max_length=30)
    link = models.URLField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Apartment(models.Model):
    '''
    temporary storage of scraped Apartment data
    '''
    source = models.ForeignKey(Source)
    school = models.ForeignKey(School)
    title = models.CharField(max_length=60)
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zip_cd = models.CharField(max_length=15, blank=True, null=True)
    lat = models.DecimalField(max_digits=12, decimal_places=6)
    long =  models.DecimalField(max_digits=12, decimal_places=6)
    phone = PhoneNumberField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    exists = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ApartmentImage(models.Model):
    apartment = models.ForeignKey(Apartment)
    link = models.CharField(max_length=200)


class ApartmentFloorPlan(models.Model):
    apartment = models.ForeignKey(Apartment)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    bed_count = models.IntegerField(choices=BED_CHOICES)
    bath_count = models.DecimalField(decimal_places=1, max_digits=5, choices=BATH_CHOICES)
    sq_ft =  models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.apartment) + ' - ' + str(self.bed_count) + ' bedroom, ' + str(self.bath_count) + \
            ' bath, ' + '($' + str(self.price) + ')'


class AmenityCrossWalk(models.Model):
    #model used to map scraped amenities to Amenity
    amenity = models.ForeignKey(Amenity)
    scrape_title = models.CharField(max_length=40)

    def __str__(self):
        return self.scrape_title


class ApartmentAmenity(models.Model):
    apartment = models.ForeignKey(Apartment)
    title = models.CharField(max_length=40)


class Log(models.Model):
    city = models.ForeignKey(City)
    apartment_name = models.CharField(max_length=100)
    link = models.URLField(null=True)
    datetime = models.DateTimeField(default=datetime.now())
    status = models.CharField(max_length=1, choices=SCRAPE_STATUS_CHOICES)
    comment = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        ordering = ['-datetime']
