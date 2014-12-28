import random

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify

from main.models import UserProfile
from school.models import School


class Company(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True, blank=True, editable=False)
    contact = models.ForeignKey(User, null=True, blank=True)
    
    # default_school is used to center the map
    default_school = models.ForeignKey(School, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('re-company-home', kwargs={'slug':self.slug})

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        '''
        set the slug based on the title field
        '''
        self.slug = slugify(self.name)
        
        super(Company, self).save(*args, **kwargs)   

    def get_random_contact(self):
        '''
        used to get a contact when no contact is listed on the Company
        '''
        members = User.objects.filter(profile__real_estate_company=self)
        contact = random.choice(members)
        return contact
        