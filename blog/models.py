import os

from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify


#need to do this to avoid circular reference on ForeignKey fields
Property = 'property.Property'
School = 'school.School'


#####images#####
def get_article_image_path(instance, filename):
  return os.path.join('blog/' + filename)


#####blog models######
class Tag(models.Model):
  '''
  used to group articles
  '''
  tag_name = models.CharField(max_length=30)

  def __str__(self):
    return self.tag_name

  class Meta:
    ordering = ['tag_name']


class Article(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL)
  school = models.ForeignKey(School, null=True, blank=True)
  property = models.ForeignKey(Property, null=True, blank=True)
  title = models.CharField(max_length=100)
  heading = models.CharField(max_length=200, null=True, blank=True)
  create_date = models.DateField(auto_now_add=True)
  body = models.TextField()
  tags = models.ManyToManyField(Tag, null=True, blank=True)
  active = models.BooleanField(default=True)
  image = models.ImageField(upload_to=get_article_image_path, null=True)
  sponsored = models.BooleanField(default=False)
  general_page = models.BooleanField(default=False)

  def __str__(self):
    return self.title

  def get_absolute_url(self):
    return reverse('blog-article', kwargs={'pk':self.id, 'slug':slugify(self.title)})

  def get_edit_url(self):
    return reverse('ca-edit-content', kwargs={'pk':self.id, 'type':'article'})


  class Meta:
    ordering = ['-create_date']
