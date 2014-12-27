from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify

School = 'school.School'


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