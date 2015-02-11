import random
import os

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from school.models import School


class Company(models.Model):
    def get_company_logo_path(instance, filename):
        return os.path.join('company/' + filename)

    name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True, blank=True, editable=False)
    contact = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,
        help_text="By choosing a contact, that contact will show on all your properties. By leaving this\
        blank, each time a property is loaded a random agent from your company will be shown. If you want \
        certain agents to be shown for certain properties, you need to set that on the Edit Property.")
    logo = models.ImageField(upload_to=get_company_logo_path, null=True, blank=True, 
        help_text="This image will show on properties that the agent has not chosen a default picture \
        through Edit Profile. If there is no agent picture nor a default company logo, a RentVersity \
        logo will be shown.")

    # default_school is used to center the map
    default_school = models.ForeignKey(School, null=True, blank=True, 
        help_text="This school will be shown when users search by your company properties.")

    def get_absolute_url(self):
        return reverse('re-company-home', kwargs={'slug':self.slug})

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        '''
        set the slug based on the title field
        '''
        self.slug = slugify(self.name).__str__()

        super(Company, self).save(*args, **kwargs)

    def get_random_contact(self):
        '''
        used to get a contact when no contact is listed on the Company
        '''
        members = get_user_model().objects.filter(real_estate_company=self)
        if members:
            contact = random.choice(members)
            return contact
        else:
            return None
