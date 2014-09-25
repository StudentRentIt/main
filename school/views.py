from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify
from django.conf import settings

from property.models import Property, PropertyRoom, Amenity, PropertyLeaseType, \
                            PropertyLeaseStart, PropertyLeaseTerm

from school.models import School, Neighborhood
from school.utils import get_school, get_school_items, get_neighborhood_items

from main.utils import get_favorites, unslugify

from blog.models import Article

from flowreport.models import SchoolSearch



def home(request):
    '''
    home page for all schools. There will be some general data about school data and also have a
    listing of all the schools that we have in our system....maybe?
    '''
    schools = School.objects.all()

    return render(request, 'schoolcontent/home.html',
                  {'schools':schools})


def school_info(request, **kwargs):
    '''
    school info shows Tier-1 and Tier-2 information about a college campus. We either are
    going to pass in a neighborhood or view the entire campus.

    If the neighborhood is passed in then we will show T1 and T2 data about the neighborhood.

    If the whole school is passed in, then we're going to see just T1 data about school.
    '''
    type = kwargs['type']
    school_slug = kwargs['slug']
    school = get_school(school_slug)

    if type == "neighborhood":
        # info page for a neighborhood
        neighborhood_slug = kwargs["n_slug"]
        neighborhood = get_object_or_404(Neighborhood, name=unslugify(neighborhood_slug))
        neighborhoods = None

        map_dict = {
            # create map varibles to determine the center and zoom
            'zoom':14,
            'lat':neighborhood.lat,
            'long':neighborhood.long,
        }

        items = get_neighborhood_items(type, neighborhood)
    elif type == "info":
        # info page for a school
        neighborhood = None
        neighborhoods = Neighborhood.objects.filter(school=school)

        map_dict = {
            # create map varibles to determine the center and zoom
            'zoom':13,
            'lat':school.lat,
            'long':school.long
        }

        items = get_school_items(type, school)

    return render(request, 'schoolcontent/info.html',
                  {'school':school, 'type':type, 'google_api_key':settings.GOOGLE_API_KEY,
                   'map_dict':map_dict, 'neighborhood':neighborhood, 'neighborhoods':neighborhoods,
                   'items':items})