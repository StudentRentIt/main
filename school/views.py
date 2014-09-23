from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from django.conf import settings

from property.models import Property, PropertyRoom, Amenity, PropertyLeaseType, \
                            PropertyLeaseStart, PropertyLeaseTerm

from school.models import School, Neighborhood
from school.utils import get_school

from main.utils import get_favorites, unslugify

from flowreport.models import SchoolSearch



def home(request):
    '''
    home page for all schools. There will be some general data about school data and also have a
    listing of all the schools that we have in our system....maybe?
    '''
    schools = School.objects.all()

    return render(request, 'schoolcontent/home.html',
                  {'schools':schools})


def school_search(request, **kwargs):
    '''
    search a school for apartments
    '''
    try:
        if kwargs['slug']:
            #school was passed in
            school = get_school(kwargs['slug'])
            slug = slugify(school.name)
            pk = school.id
    except KeyError:
        school = None
        slug = None
        pk = None

    if request.user.is_staff:
        properties = Property.objects.filter(school=pk, lat__isnull=False, long__isnull=False)
    else:
        # exclude internal properties if not staff
        properties = Property.objects.filter(school=pk, lat__isnull=False, long__isnull=False, internal=False)

    # remove the property from the list if it is hidden for the user
    if request.user.is_authenticated():
        for p in properties:
            if p.is_hidden(request.user):
                properties = properties.exclude(id=p.id)

    rooms = PropertyRoom.objects.filter(property__in=properties).exclude(lease_start=3) #available
    favorited = get_favorites(request.user)
    modal_title = "Find Housing, Apartments, Subleases and Information"

    #save the search for metrics
    if pk:
        school = get_object_or_404(School, id=pk)
        search = SchoolSearch()
        search.school = school
        search.save()

    lease_types = PropertyLeaseType.objects.filter(active=True)
    lease_starts = PropertyLeaseStart.objects.filter(active=True)
    lease_terms = PropertyLeaseTerm.objects.filter(active=True)
    special_amenities = Amenity.objects.filter(special=True)

    #if the request is a POST, filter the properties. If not, show all properties for the school.
    if request.method == "POST":
        '''
        gather the post data filters. There are a couple different types of ways
        we gather the post data. The first is through normal text input which gives
        us a single value for the post data. Another way is through a list of values
        which is passed in by the user choosing multiple values

        this section is for the multi valued post variables. The choices are passed
        in by concatenating a string and then splitting the values
        '''

        # no longer use the following criteria in search
        '''
        lease_type_string = request.POST['leaseType']
        lease_type_list = lease_type_string.split(", ")
        lease_term_string = request.POST['leaseTerm']
        lease_term_list = lease_term_string.split(", ")
        lease_start_string = request.POST['leaseStart']
        lease_start_list = lease_start_string.split(", ")
        '''

        #take the post data and create variables
        min_price = request.POST['minPrice']
        max_price = request.POST['maxPrice']
        min_bath = request.POST['minBath']
        max_bath = request.POST['maxBath']
        min_bed = request.POST['minBed']
        max_bed = request.POST['maxBed']
        # keyword = request.POST['keyword']

        #clean price inputs
        min_price = min_price.replace("$", "")
        max_price = max_price.replace("$", "")
        min_price = min_price.replace(",", "")
        max_price = max_price.replace(",", "")

        #clean bedroom input to allow "studio"
        if min_bed == "studio":
            min_bed = "0"
        if max_bed == "studio":
            max_bed = "0"

        # checkbox post needs to be set to blank if unchecked
        # not using this currently after RentVersity change
        # try:
        #     business = request.POST['business']
        # except:
        #     business = ''

        '''
        filter rooms based on post filters. We'll get a list of rooms and then
        filter the properties based on which rooms we have
        '''
        if min_price:
            rooms = rooms.filter(price__gte=min_price)

        if max_price:
            rooms = rooms.filter(price__lte=max_price)

        if min_bath:
            rooms = rooms.filter(bath_count__gte=min_bath)

        if max_bath:
            rooms = rooms.filter(bath_count__lte=max_bath)

        if min_bed:
            rooms = rooms.filter(bed_count__gte=min_bed)

        if max_bed:
            rooms = rooms.filter(bed_count__lte=max_bed)

        # if keyword:
        #     '''
        #     get the keyword and search the property fields for the keyword.
        #     then need to filter the rooms based on that property
        #     '''
        #     keyword_properties = Property.get_keyword_property(keyword)
        #     rooms = rooms.filter(property__in=keyword_properties)

        # no longer use the following criteria in searches
        '''
        if lease_start_string:
            rooms = rooms.filter(lease_start__in=lease_start_list)

        if lease_type_string:
            lease_type_properties = Property.objects.filter(lease_type__in=lease_type_list)
            rooms = rooms.filter(property__in=lease_type_properties)

        if lease_term_string:
            lease_term_properties = Property.objects.filter(lease_term__in=lease_term_list)
            rooms = rooms.filter(property__in=lease_term_properties)
        '''

        #create list of properties that are filtered
        property_filtered_list = []
        for r in rooms:
            property_filtered_list.append(r.property.id)

        #filter properties and if the business checkbox was checked include businesses
        properties = properties.filter(id__in=property_filtered_list)

        # if business:
        #     businesses = Property.objects.filter(school=pk, type="BUS")
        #     properties = properties | businesses

    #if location passed in, get the coordinates to center map
    if pk:
        lat = school.lat
        long = school.long
    else: # default to Texas State, for now
        lat = 29.87
        long = -97.93
        school = None

    return render(request, 'schoolcontent/search.html',
        {'lat':lat, 'long':long, 'school':school, 'url_prefix':'search',
        'modal_title':modal_title, 'properties':properties, 'favorited':favorited, 'rooms':rooms,
        'lease_types':lease_types, 'lease_terms':lease_terms, 'lease_starts':lease_starts,
        'special_amenities':special_amenities, 'google_api_key':settings.GOOGLE_API_KEY})



def school_info(request, **kwargs):
    '''
    school info shows Tier-1 and Tier-2 information about a college campus. We either are
    going to pass in a neighborhood or view the entire campus.

    If the neighborhood is passed in then we will show T1 and T2 data about the neighborhood.

    If the whole school is passed in, then we're going to see just T1 data about school.
    '''
    school_slug = kwargs['slug']
    school = get_school(school_slug)

    type = kwargs['type']

    if type == "neighborhood":
        # info page for a neighborhood
        neighborhood_slug = kwargs["n_slug"]
        neighborhoods = None
        neighborhood = get_object_or_404(Neighborhood, name=unslugify(neighborhood_slug))
        map_dict = {
            'zoom':14,
            'lat':neighborhood.lat,
            'long':neighborhood.long
        }

    elif type == "info":
        # info page for a school
        neighborhood = None
        neighborhoods = Neighborhood.objects.filter(school=school)
        map_dict = {
            'zoom':13,
            'lat':school.lat,
            'long':school.long
        }


    return render(request, 'schoolcontent/info.html',
                  {'school':school, 'type':type, 'google_api_key':settings.GOOGLE_API_KEY,
                   'map_dict':map_dict, 'neighborhood':neighborhood, 'neighborhoods':neighborhoods})