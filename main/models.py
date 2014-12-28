import os
from decimal import Decimal
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from localflavor.us.models import PhoneNumberField, USStateField


#need to do this to avoid circular reference on ForeignKey fields
Property = 'property.Property'
Service = 'property.Service'
Company = 'realestate.Company'


USER_TYPE_CHOICES = (
    ('STU', 'Student'),
    ('BOW', 'Business Owner'),
    ('MGR', 'Landlord/Manager')
)

'''*****************************************************************************
General Models
'''
class UserProfile(models.Model):

    def get_user_image_path(instance, filename):
        return os.path.join('user/', filename)

    user = models.OneToOneField(User, related_name='profile')
    user_type = models.CharField(max_length=30, null=True, blank = True,
        choices=USER_TYPE_CHOICES)
    pic = models.ImageField(upload_to=get_user_image_path, null=True, blank = True)
    real_estate_company = models.ForeignKey(Company, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)

    def get_groups(self):
        '''
        return list of groups that a user is in. Also can be used to see if a
        user is any group.
        '''
        from search.models import GroupMember
        gm_objects = GroupMember.objects.filter(user=self.user)

        groups = []
        for g in gm_objects:
            groups.append(g.group)

        return groups

    def get_group_properties(self):
        '''
        return a list of PROPERTIES (note, not GroupProperty) that a user has
        in their groups
        '''
        from search.models import GroupProperty, GroupMember
        gm_list = GroupMember.objects.filter(user=self.user)

        # GroupMember > Group > GroupProperty > Property
        group_list = []
        group_property_list = []
        property_list = []

        for gm in gm_list:
            group_list.append(gm.group)

        group_property_list = GroupProperty.objects.filter(group__in=group_list)

        for gp in group_property_list:
            property_list.append(gp.property)

        return property_list

    def __str__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    '''
    Create User Profile when a User is created so that we can update the profile
    in the same scope
    '''
    if created:
        UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)


class TeamMember(models.Model):

    def get_teammember_image_path(instance, filename):
        return os.path.join('teammember/', filename)

    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    picture = models.ImageField(upload_to=get_teammember_image_path, null=True, blank=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=40)
    state = USStateField()
    link = models.CharField(max_length=100, null=True, blank=True)
    multi_university = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ', ' + self.state


class Contact(models.Model):
    property = models.ForeignKey(Property, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = PhoneNumberField(null=True)
    subject = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    contact_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.subject


class Payment(models.Model):
    payment_date = models.DateField(auto_now_add=True)
    property = models.ForeignKey(Property, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    services = models.ManyToManyField(Service, null=True, blank=True)
    recurring = models.BooleanField(default=False)
    amount = models.IntegerField()

