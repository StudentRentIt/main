from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from property.models import Property


class Group(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('search-group-view', kwargs={'pk':self.id})


class GroupMember(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    # TODO: user characteristics such as admin

    class Meta:
        unique_together = ('user', 'group',)

    def __str__(self):
        return self.user.username


class GroupProperty(models.Model):
    # a property that has been added into a group for comments/viewing
    property = models.ForeignKey(Property)
    group = models.ForeignKey(Group)

    class Meta:
        unique_together = ('property', 'group',)

    def __str__(self):
        return str(self.property) + ' for ' + str(self.group)


class GroupComment(models.Model):
    '''
    leave group comments for certain properties
    '''
    group_property = models.ForeignKey(GroupProperty)
    author = models.ForeignKey(GroupMember)
    text = models.CharField(max_length=200)
    create_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author) + ' ' + self.text