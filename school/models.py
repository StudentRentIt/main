from django.db import models
import os

from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from main.models import City
from localflavor.us.models import PhoneNumberField

#need to do this to avoid circular reference on ForeignKey fields
Property = 'property.Property'


def get_school_image_path(instance, filename):
    return os.path.join('school/' + str(instance.id), filename)

def get_deal_image_path(instance, filename):
    return os.path.join('deals/' + str(instance.school.id) , filename)

def get_event_image_path(instance, filename):
    return os.path.join('events/' + str(instance.school.id) , filename)


class School(models.Model):
    '''
    information about the schools that we have in our system
    '''
    city = models.ForeignKey(City, null=True, blank=True)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100, null=True, blank=True)
    mascot = models.CharField(max_length=50, null=True, blank=True)
    long =  models.DecimalField(max_digits=10, decimal_places=6)
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    image = models.ImageField(upload_to=get_school_image_path, null=True)

    def get_absolute_url(self):
        return reverse('search', kwargs={'slug':slugify(self.name)})

    def get_info_url(self):
        # url for the school info page
        return reverse('school-info', kwargs={'slug':slugify(self.name),
                                              'type':'info'})

    def __str__(self):
        return self.name


class Neighborhood(models.Model):
    '''
    be able to split up a school into neighborhoods to filter data and searches
    '''
    school = models.ForeignKey(School)
    name = models.CharField(max_length=30)
    lat =  models.DecimalField(max_digits=10, decimal_places=6)
    long = models.DecimalField(max_digits=10, decimal_places=6)

    def get_absolute_url(self):
        return reverse('school-neighborhood', kwargs={'slug':slugify(self.school.name),
                                                      'type':'neighborhood',
                                                      'n_slug':slugify(self.name)})

    def __str__(self):
        return self.name


class SchoolBaseItem(models.Model):
    '''
    used as a base class for school items. We need to force fields in common in order
    to display them effectively on the front-end
    '''
    create_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User)
    school = models.ForeignKey(School)
    title = models.CharField(max_length=50)
    description = models.TextField()
    heading = models.CharField(max_length=200, null=True, blank=True)
    active = models.BooleanField(default=True)
    sponsored = models.BooleanField(default=False)

    class Meta:
        abstract = True
        ordering = ['-create_date']


class Deal(SchoolBaseItem):
    '''
    deals or promotions for local businesses or apartments
    '''
    image = models.ImageField(upload_to=get_deal_image_path, null=True, blank=True)
    property = models.ForeignKey(Property)

    class Meta:
        ordering = ['-sponsored', '-id']

    def get_edit_url(self):
        return reverse('ca-edit-content', kwargs={'pk':self.id, 'type':'deal'})

    def __str__(self):
        return self.property.title + ' - ' + self.title


class Event(SchoolBaseItem):
    '''
    events that are listed. Will show up in the school sections.
    '''
    image = models.ImageField(upload_to=get_event_image_path, null=True, blank=True)
    property = models.ForeignKey(Property, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=100)

    class Meta:
        ordering = ['-sponsored', '-id']

    def get_edit_url(self):
        return reverse('ca-edit-content', kwargs={'pk':self.id, 'type':'event'})

    def __str__(self):
        return self.title