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
        return reverse('search', kwargs={'pk':self.id, 'slug':slugify(self.name)})

    def __str__(self):
        return self.name


class Deal(models.Model):
    '''
    deals or promotions for local businesses or apartments
    '''
    user = models.ForeignKey(User)
    property = models.ForeignKey(Property)
    title = models.CharField(max_length=50)
    description= models.TextField()
    image = models.ImageField(upload_to=get_deal_image_path, null=True, blank=True)
    active = models.BooleanField(default=True)
    sponsored = models.BooleanField(default=False)

    class Meta:
        ordering = ['-sponsored', '-id']

    def get_school(self):
        # return the school that the deal belongs to
        property = self.property
        school = property.school
        return school

    def __str__(self):
        return self.property.title + ' - ' + self.title


class Event(models.Model):
    '''
    events that are listed. Will show up in the school sections.
    '''
    user = models.ForeignKey(User)
    property = models.ForeignKey(Property, null=True, blank=True)
    school = models.ForeignKey(School)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_event_image_path, null=True, blank=True)
    active = models.BooleanField(default=True)
    sponsored = models.BooleanField(default=False)

    class Meta:
        ordering = ['-sponsored', '-id']

    def __str__(self):
        return self.title