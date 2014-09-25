from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Group(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('search-group-manage', kwargs={'pk':self.id})


class GroupMember(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(Group)
    # TODO: user characteristics such as admin

    class Meta:
        unique_together = ('user', 'group',)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    author = models.ForeignKey(GroupMember)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.author + ' ' + self.text