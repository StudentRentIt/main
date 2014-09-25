from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class GroupMember(models.Model):
    user = models.ForeignKey(User)
    # TODO: user characteristics such as admin

    def __str__(self):
        return self.user


class Group(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('search-group-manage', kwargs={'pk':self.id})


class Comment(models.Model):
    author = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.author + ' ' + self.text