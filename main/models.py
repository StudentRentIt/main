import os
import random
from decimal import Decimal
from django.db import models
from django.db.models import Q, Avg
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from localflavor.us.models import PhoneNumberField, USStateField

'''*****************************************************************************
Choice Field Lists
'''
SERVICE_TYPE_CHOICES = (
    ('O', 'One-Time'),
    ('R', 'Recurring'),
)
AMENITY_TYPE_CHOICES = (
    ('CMW', 'In Your Apartment'),
    ('BIN', 'Bills Included'),
    ('PRO', 'Property Amenities'),
)
USER_TYPE_CHOICES = (
    ('STU', 'Student'),
    ('BOW', 'Business Owner'),
    ('MGR', 'Landlord/Manager')
)
PROPERTY_TYPE_CHOICES = (
    ('APT', 'Apartment'),
    ('BUS', 'Business')
)
BED_CHOICES = (
    (0, 'studio'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
)
BATH_CHOICES = (
    (Decimal("1.0"), "1"),
    (Decimal("1.5"), "1.5"),
    (Decimal("2.0"), "2"),
    (Decimal("2.5"), "2.5"),
    (Decimal("3.0"), "3"),
    (Decimal("3.5"), "3.5"),
    (Decimal("4.0"), "4"),
    (Decimal("4.5"), "4.5"),
    (Decimal("5.0"), "5"),
    (Decimal("5.5"), "5.5"),
    (Decimal("6.0"), "6"),
    (Decimal("6.5"), "6.5"),
)
BOOL_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)

'''*****************************************************************************
Upload Paths
'''
def get_article_image_path(instance, filename):
    if instance.school:
        group = str(instance.school.id)
    else:
        group = 'general'
    return os.path.join('blog/' + group, filename)

def get_deal_image_path(instance, filename):
    return os.path.join('deals/' + str(instance.school.id) , filename)

def get_roommate_image_path(instance, filename):
    return os.path.join('roommates/' + str(instance.school.id) , filename)

def get_event_image_path(instance, filename):
    return os.path.join('roommates/' + str(instance.school.id) , filename)

def get_property_image_path(instance, filename):
    return os.path.join('property/' + str(instance.property.id), filename)

def get_school_image_path(instance, filename):
    return os.path.join('school/' + str(instance.id), filename)

def get_amenity_image_path(instance, filename):
    return os.path.join('amenity/', filename)

def get_teammember_image_path(instance, filename):
    return os.path.join('teammember/', filename)


'''*****************************************************************************
General Models
'''
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    user_type = models.CharField(max_length=30, null=True, blank = True,
        choices=USER_TYPE_CHOICES)

    def __unicode__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    '''
    Create User Profile when a User is created so that we can update the profile
    in the same scope
    '''
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)


class TeamMember(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    picture = models.ImageField(upload_to=get_teammember_image_path, null=True, blank=True)

    def __str__(self):
        return self.name

class Amenity(models.Model):
    amenity = models.CharField(max_length=50)
    type = models.CharField(max_length=3, choices=AMENITY_TYPE_CHOICES, null=True, blank=True)
    image = models.ImageField(upload_to=get_amenity_image_path, null=True, blank=True)
    link = models.CharField(max_length=100, null=True, blank=True)
    special = models.BooleanField(default=False)

    def __str__(self):
        return self.amenity

    class Meta:
        ordering = ['amenity']


class City(models.Model):
    name = models.CharField(max_length=40)
    state = USStateField()
    link = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name + ', ' + self.state


class School(models.Model):
    city = models.ForeignKey(City, null=True, blank=True)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100, null=True, blank=True)
    mascot = models.CharField(max_length=50, null=True, blank=True)
    long =  models.DecimalField(max_digits=10, decimal_places=6)
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    image = models.ImageField(upload_to=get_school_image_path, null=True)

    def get_absolute_url(self):
        return reverse('search', kwargs={'pk':self.id, 'slug':slugify(self.name)})

    def __str__(self):
        return self.name


'''*****************************************************************************
Property Models
'''

class Service(models.Model):
    '''
    We provide certain services to properties and that is one way that we generate
    revenue.
    '''
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    service_type = models.CharField(max_length=1, choices=SERVICE_TYPE_CHOICES, default="R")
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Package(models.Model):
    '''
    Packages contain a grouping of services and offer properties a way to purchase
    multiple services at a discounted rate
    '''
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    services = models.ManyToManyField(Service, null=True, blank=True)
    active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    similar_property_strength = models.IntegerField(default=0)

    class Meta:
        ordering = ['-order']

    def __str__(self):
        return self.title

class PropertyLeaseType(models.Model):
    lease_type = models.CharField(max_length=20)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['lease_type']

    def __str__(self):
        return self.lease_type


class PropertyLeaseTerm(models.Model):
    lease_term = models.CharField(max_length=20)
    lease_term_short = models.CharField(max_length=5, null=True, blank=True)
    active = models.BooleanField(default=True)
    order = models.IntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.lease_term


class PropertyLeaseStart(models.Model):
    lease_start = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    order = models.IntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.lease_start


class Property(models.Model):
    #REQUIRED FIELDS - these are displayed on the first Add New Property section
    school= models.ForeignKey(School)
    type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES, default="APT")
    user = models.ForeignKey(User, null=True)
    title = models.CharField(max_length=30)
    addr = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    state = USStateField()
    zip_cd = models.CharField(max_length=15)

    # hidden fields on forms
    lat = models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True)
    long =  models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True)
    active = models.BooleanField(default=True)
    sponsored = models.BooleanField(default=False)
    top_list = models.BooleanField(default=False)

    # optional detail fields for users to fill out after basic property has been created
    lease_type = models.ManyToManyField(PropertyLeaseType, null=True, blank=True)
    lease_term = models.ManyToManyField(PropertyLeaseTerm, null=True, blank=True)
    amenities = models.ManyToManyField(Amenity, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    special = models.TextField(null=True, blank=True)
    fee_desc = models.TextField(null=True, blank=True)

    #contact fields
    contact_first_name = models.CharField(max_length=50, null=True, blank=True)
    contact_last_name = models.CharField(max_length=50, null=True, blank=True)
    contact_phone = PhoneNumberField(null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)

    services = models.ManyToManyField(Service, null=True, blank=True)
    package = models.ForeignKey(Package, null=True, blank=True)

    class Meta:
        ordering = ['-top_list', '-sponsored', '-package__order', 'id']

    def __str__(self):
        return self.title

    def get_keyword_property(keyword):
        properties = Property.objects.filter(
            Q(title__icontains=keyword) | Q(description__icontains=keyword) |
            Q(special__icontains=keyword) | Q(fee_desc__icontains=keyword))
        return properties

    def get_full_address(self):
        full_address = self.addr + ' ' + self.city + ', ' + self.state + ' ' + self.zip_cd
        return full_address

    def avg_price(self):
        avg_price = PropertyRoom.objects.filter(property=self).aggregate(Avg('price'))
        return avg_price.get('price__avg')

    def get_absolute_url(self):
        return reverse('property', kwargs={'pk':self.id, 'slug':slugify(self.title)})

    def has_community(self):
        '''
        Check to see if the property has any community items
        '''
        has_community = False

        articles = Article.objects.filter(property=self)
        events = Event.objects.filter(property=self)
        roommates = Roommate.objects.filter(property=self)
        deals = Deal.objects.filter(property=self)

        if articles or events or roommates or deals:
            has_community = True

        return has_community

    def get_related_properties(self):
        '''
        get a list of eligible properties, add each property to the pot the number
        of times it has in the strength. Take 3 properties at random from the pot
        and add them to similar properties! Easy as pie.
        '''

        if Package.objects.all():
            '''
            if there are no packages then just take a list of all properties
            include free only if there are not enough properties that have packages
            '''
            if Property.objects.filter(package__isnull=False).count() > 15:
                include_free = False
            else:
                include_free = True

            # create the property pot which includes the properties that are eligible
            property_pot = []
            if include_free:
                elig_properties = Property.objects.filter(school=self.school, type="APT")
            else:
                elig_properties = Property.objects.filter(school=self.school, type="APT", package__isnull=False)

            for p in elig_properties:
                if p.package:
                    x = p.package.similar_property_strength
                else:
                    x = 1

                for _i in range(x):
                    property_pot.append(p)

                #get the 3 related properties
                random.shuffle(property_pot)
                related_properties = []
                for p in property_pot:
                    if p not in related_properties:
                        related_properties.append(p)
                    if len(related_properties) > 2:
                        break

            return related_properties
        else:
            related_properties = Property.objects.filter(school=self.school, type="APT").order_by("?")[:3]
            return related_properties


class PropertyImage(models.Model):
    property = models.ForeignKey(Property)
    image = models.ImageField(upload_to=get_property_image_path)
    caption = models.CharField(max_length=40, null=True, blank=True)
    main = models.BooleanField(default=False)
    floorplan = models.BooleanField(default=False)
    order = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-main', 'order', 'caption']


class PropertyVideo(models.Model):
    property = models.ForeignKey(Property)
    video_link = models.CharField(max_length=300)
    main = models.BooleanField(default=False)
    order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.property.title

    class Meta:
        ordering = ['-main', 'order']


class PropertyRoom(models.Model):
    property = models.ForeignKey(Property)
    lease_start = models.ForeignKey(PropertyLeaseStart, default=2) #default will change on the season/year
    price = models.DecimalField(decimal_places=2, max_digits=8)
    bed_count = models.IntegerField(choices=BED_CHOICES)
    bath_count = models.DecimalField(decimal_places=1, max_digits=5, choices=BATH_CHOICES)
    sq_ft =  models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.bed_count) + ' bedroom, ' + str(self.bath_count) + \
            ' bath, ' + '($' + str(self.price) + ')'

    class Meta:
        ordering = ['price', 'bed_count']


class PropertyFavorite(models.Model):
    property = models.ForeignKey(Property)
    user = models.ForeignKey(User)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.user) + ' - ' + self.property.title


class PropertyReserve(models.Model):
    property = models.ForeignKey(Property)
    user = models.ForeignKey(User, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    phone_number = PhoneNumberField(null=True)
    floor_plan = models.ForeignKey(PropertyRoom)
    move_in_date = models.DateField()
    felony = models.BooleanField(choices=BOOL_CHOICES, default=False)
    evicted = models.BooleanField(choices=BOOL_CHOICES, default=False)
    credit = models.BooleanField(choices=BOOL_CHOICES, default=False)
    agree = models.BooleanField(choices=BOOL_CHOICES, default=False)
    reserve_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-reserve_date']


class PropertySchedule(models.Model):
    property = models.ForeignKey(Property)
    user = models.ForeignKey(User, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    phone_number = PhoneNumberField(null=True)
    create_date = models.DateField(auto_now_add=True)
    schedule_date = models.DateField()
    schedule_time = models.TimeField()

    class Meta:
        ordering = ['-create_date']


'''*****************************************************************************
School Info Models
'''
class Tag(models.Model):
    tag_name = models.CharField(max_length=30)

    def __str__(self):
        return self.tag_name

    class Meta:
        ordering = ['tag_name']


class Article(models.Model):
    user = models.ForeignKey(User)
    school = models.ForeignKey(School, null=True, blank=True)
    property = models.ForeignKey(Property, null=True, blank=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to=get_article_image_path, null=True)
    sponsored = models.BooleanField(default=False)
    general_page = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-article', kwargs={'pk':self.id, 'slug':slugify(self.title)})

    class Meta:
        ordering = ['-create_date']


class Deal(models.Model):
    '''
    can only be entered by a business owner
    '''
    user = models.ForeignKey(User)
    school = models.ForeignKey(School)
    property = models.ForeignKey(Property)
    title = models.CharField(max_length=50)
    description= models.TextField()
    image = models.ImageField(upload_to=get_deal_image_path, null=True, blank=True)
    active = models.BooleanField(default=True)
    sponsored = models.BooleanField(default=False)

    class Meta:
        ordering = ['-sponsored', '-id']

    def __str__(self):
        return self.property.title + ' - ' + self.title


class Event(models.Model):
    user = models.ForeignKey(User)
    school = models.ForeignKey(School)
    property = models.ForeignKey(Property, null=True, blank=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_event_image_path, null=True, blank=True)
    active = models.BooleanField(default=True)
    sponsored = models.BooleanField(default=False)

    class Meta:
        ordering = ['-sponsored', '-id']

    def __str__(self):
        return self.title


class Roommate(models.Model):
    user = models.ForeignKey(User)
    school = models.ForeignKey(School)
    property = models.ForeignKey(Property, null=True, blank=True)
    name = models.CharField(max_length=100)
    message = models.TextField()
    phone = PhoneNumberField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(upload_to=get_roommate_image_path, null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


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

