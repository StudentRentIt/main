import os
from decimal import Decimal
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from localflavor.us.models import PhoneNumberField, USStateField


#need to do this to avoid circular reference on ForeignKey fields
Property = 'property.Property'
Service = 'property.Service'


USER_TYPE_CHOICES = (
    ('STU', 'Student'),
    ('BOW', 'Business Owner'),
    ('MGR', 'Landlord/Manager')
)

'''*****************************************************************************
General Models
'''
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    user_type = models.CharField(max_length=30, null=True, blank = True,
        choices=USER_TYPE_CHOICES)

    def in_group(self):
        # determine if a user is in a search group
        from search.models import GroupMember
        if GroupMember.objects.filter(user=self.user):
            return True
        else:
            return False

    def asdf(self):
        '''
        return a list of all properties that a user can't add to their
        group search list because they have already added it to all their groups
        '''

        # get user's groups
        from search.models import GroupProperty, GroupMember
        groups = GroupMember.objects.filter(user=self.user)
        group_properties = GroupProperty.objects.filter(group__in=groups)

        # get which group proeperties have been added to all the user's groups
        group_count = len(groups)

        # put all the properties from all the groups into an array
        all_group_property_list = []
        for g in group_properties:
            all_group_property_list.append(g)

        '''
        get the exclusion list by seeing if the amount of instances is
        equal to the length of groups
        '''
        exclusion_list = []
        for p in all_group_property_list:
            count = all_group_property_list.count(p)
            if count == group_count and p not in exclusion_list:
                exclusion_list.append(p)


        return all_group_property_list




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

