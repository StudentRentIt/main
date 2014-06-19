from django.db import models

from main.models import BATH_CHOICES, BED_CHOICES, City, School

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


class Apartment(models.Model):
    '''
    temporary storage of scraped Apartment data
    '''
    school = models.ForeignKey(School)
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=80, blank=True, null=True)
    zip_cd = models.CharField(max_length=15, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=1, choices=SOURCE_CHOICES)
    source_link = models.URLField()


class ApartmentPic(models.Model):
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


class ApartmentAmenity(models.Model):
    apartment = models.ForeignKey(Apartment)
    # TODO: switch to lookup field once we have a good set of feature titles
    title = models.CharField(max_length=40)


class ScrapeLog(models.Model):
    city = models.ForeignKey(City)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=SCRAPE_STATUS_CHOICES)