import random

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.utils.text import slugify

from school.models import School


class Company(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True, blank=True, editable=False)
    contact = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)

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
        members = get_user_model().objects.filter(real_estate_company=self)
        if members:
            contact = random.choice(members)
            return contact
        else:
            return None
