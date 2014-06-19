from django.db import models

from main.models import Property, School, Package


PROPERTY_IMPRESSION_CHOICES = (
    ('P', 'Property Page'),
    ('S', 'Property Page Similar'),
    ('B', 'School Side Bar'),
    ('L', 'List View'),
    ('M', 'Map View Click'),
    ('F', 'Favorite'),
)

SCHOOL_IMPRESSION_CHOICES = (
    ('D', 'Deal'),
    ('E', 'Event'),
    ('A', 'Article Seen'),
    ('O', 'Article Open'),
)

SCHOOL_ITEM_CHOICES = (
    ('A', 'Article'),
    ('D', 'Deal'),
    ('E', 'Event'),
)


class Audience(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Report(models.Model):
    '''
    The report model will contain metadata about reports and will
    function as the report dictionary.
    '''
    title = models.CharField(max_length=30)
    desc = models.TextField(null=True, blank=True)
    audience = models.ManyToManyField(Audience, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class PropertyImpression(models.Model):
    '''
    Impression data for Property Items
    '''
    property = models.ForeignKey(Property, db_index=True)
    imp_property_package = models.ForeignKey(Package, blank=True, null=True)
    imp_property_sponsored = models.BooleanField(default=False)
    imp_type = models.CharField(max_length=1, choices=PROPERTY_IMPRESSION_CHOICES)
    imp_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.property) + ' - ' + self.get_imp_type_display()

    class Meta:
        ordering = ['-imp_date', 'property__title']


class SchoolItemImpression(models.Model):
    '''
    Impression data for School Items
    '''
    item_type = models.CharField(max_length=1, choices=SCHOOL_ITEM_CHOICES)
    item_id = models.IntegerField()
    imp_type = models.CharField(max_length=1, choices=SCHOOL_IMPRESSION_CHOICES)
    imp_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.get_type_display() + ' - ' + str(self.item_id)

    class Meta:
        ordering = ['-imp_date']


class SchoolSearch(models.Model):
    '''
    Register when a school search has bene performed
    '''
    school = models.ForeignKey(School)
    search_date = models.DateField(auto_now_add=True)