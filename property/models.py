import os
import random

from decimal import Decimal

from django.db import models
from django.db.models import Avg, Q, Max, Min
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from localflavor.us.models import PhoneNumberField, USStateField
from school.models import School, Neighborhood
from property.utils import get_place_data, get_place_detail_data
from realestate.models import Company


#property choice lists
BOOL_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)
SERVICE_TYPE_CHOICES = (
    ('O', 'One-Time'),
    ('R', 'Recurring'),
)
AMENITY_TYPE_CHOICES = (
    ('CMW', 'In Your Apartment'),
    ('BIN', 'Bills Included'),
    ('PRO', 'Property Amenities'),
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


#image paths
def get_property_image_path(instance, filename):
    return os.path.join('property/' + str(instance.property.id), filename)

def get_amenity_image_path(instance, filename):
    return os.path.join('amenity/', filename)


#####property models######
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
    neighborhood = models.ForeignKey(Neighborhood, null=True, blank=True)
    type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES, default="APT")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    title = models.CharField(max_length=50)
    addr = models.CharField(max_length=1000)
    city = models.CharField(max_length=1000)
    state = USStateField()

    # hidden fields on forms
    lat = models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True)
    long =  models.DecimalField(max_digits=12, decimal_places=6, null=True, blank=True)
    active = models.BooleanField(default=True)
    sponsored = models.BooleanField(default=False)
    top_list = models.BooleanField(default=False)

    # optional detail fields for users to fill out after basic property has been created
    place_id = models.CharField(max_length=30, blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    zip_cd = models.CharField(max_length=15, blank=True, null=True)
    lease_type = models.ManyToManyField(PropertyLeaseType, null=True, blank=True)
    lease_term = models.ManyToManyField(PropertyLeaseTerm, null=True, blank=True)
    amenities = models.ManyToManyField(Amenity, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    special = models.TextField(null=True, blank=True)
    fee_desc = models.TextField(null=True, blank=True)
    internal = models.BooleanField(default=False)
    contact_user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, 
        related_name="property_contact_user")

    services = models.ManyToManyField(Service, null=True, blank=True)
    package = models.ForeignKey(Package, null=True, blank=True)
    real_estate_company = models.ForeignKey(Company, null=True, blank=True)

    class Meta:
        ordering = ['-top_list', '-sponsored', '-package__order', 'id']

    def __str__(self):
        return self.title

    def get_contact_user(self):
        '''
        the property can have a responsible contact in a variety of ways, in this order
        #1 if the property has a contact_user
        #2 if the property has a real_estate_company with contact_user
        #3 if the proeprty has a real_estate_company but no contact_user,
            get a random member of the Real Estate Company
        '''
        if self.contact_user:
            contact_user = self.contact_user
        elif self.real_estate_company:
            if self.real_estate_company.contact:
                contact_user = self.real_estate_company.contact
            elif self.real_estate_company and not self.real_estate_company.contact:
                contact_user = self.real_estate_company.get_random_contact()
            else:
                return None
        else:
            return None

        return contact_user

    def get_keyword_property(keyword):
        properties = Property.objects.filter(
            Q(title__icontains=keyword) | Q(description__icontains=keyword) |
            Q(special__icontains=keyword) | Q(fee_desc__icontains=keyword))
        return properties

    def get_full_address(self):
        # provide a uniform way to display a full full_address
        if self.addr and self.city and self.state and self.zip_cd:
            full_address = self.addr + ' ' + self.city + ', ' + self.state + ' ' + self.zip_cd
            return full_address
        else:
            return None

    def avg_price(self):
        avg_price = PropertyRoom.objects.filter(property=self).aggregate(Avg('price'))
        return avg_price.get('price__avg')

    def low_price(self):
        p = PropertyRoom.objects.filter(property=self).aggregate(Min('price'))
        return p.get('price__min')

    def high_price(self):
        p = PropertyRoom.objects.filter(property=self).aggregate(Max('price'))
        return p.get('price__max')

    def get_absolute_url(self):
        return reverse('property', 
            kwargs={'pk':self.id, 'slug':slugify(self.title)})

    def get_edit_url(self):
        return reverse('ca-edit-property', kwargs={'pk':self.id})

    def has_community(self):
        # check to see if the property has any community items
        from blog.models import Article
        from school.models import Event, Roommate, Deal

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
        and add them to similar properties
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

    def get_place_id(self):
        '''
        Google Places API uses a place_id for individual places. Need to get that place ID so that
        we can use it with getting various data items from Google. Store the place_id on the property
        so that we don't have to run the API each time if we already have the place_id
        '''

        # if the property already has a place_id in our database, get it. If not, use the Google
        # API to get the place_id
        place_id = self.place_id

        if not place_id:
            # get the data and then save the place id to the property
            data = get_place_data(self)
            status = data.get('status')
            if status == 'OK':
                if data.get('results'):
                    place_id = data.get('results')[0].get('place_id')
                    self.place_id = place_id
                    self.save()

        return place_id

    def get_place_rating(self):
        '''
        get the google place rating for the given property. This is not meant
        to be called many times on a page, we should store the rating as a field
        on the model
        '''
        data = get_place_data(self)
        status = data.get('status')
        if status == 'OK':
            if data.get('results'):
                rating = data.get('results')[0].get('rating')
                return rating

    def get_place_review_details(self):
        '''
        returns the rating details for a specific property
        '''
        if self.place_id:
            data = get_place_detail_data(self)
            status = data.get('status')
            if status == 'OK':
                if data.get('result'):
                    reviews = data.get('result').get('reviews')

                    return reviews

    def is_hidden(self, user):
        '''
        determines if a property is hidden for the current user
        '''
        from property.models import PropertyHidden
        try:
            if PropertyHidden.objects.get(property=self, user=user):
                return True
        except:
            return False

    def get_distance_from_campus(self):
        '''
        get the distance from campus center
        '''
        from main.utils import distance

        if self.lat and self.long:
            school_loc = [self.school.lat, self.school.long]
            prop_loc = [self.lat, self.long]
            d = distance(school_loc, prop_loc)
            return d


class PropertyImage(models.Model):
    property = models.ForeignKey(Property)
    image = models.ImageField(upload_to=get_property_image_path, null=True, blank=True)
    image_link = models.URLField(null=True, blank=True)
    caption = models.CharField(max_length=40, null=True, blank=True)
    main = models.BooleanField(default=False)
    floorplan = models.BooleanField(default=False)
    order = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-main', 'order', 'caption']

    def get_url(self):
        if self.image_link:
            return self.image_link
        else:
            return self.image.url


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
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.user) + ' - ' + self.property.title


class PropertyHidden(models.Model):
    # used to hide certain properties from searches by a specific user
    property = models.ForeignKey(Property)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)


class PropertyReserve(models.Model):
    property = models.ForeignKey(Property)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    phone_number = PhoneNumberField(null=True)
    create_date = models.DateField(auto_now_add=True)
    schedule_date = models.DateField()
    schedule_time = models.TimeField()

    class Meta:
        ordering = ['-create_date']

        