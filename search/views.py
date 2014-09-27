from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse

from search.forms import GroupForm
from search.models import GroupMember, Group, GroupProperty, GroupComment
from school.models import School, Neighborhood
from school.utils import get_school, get_school_items, get_neighborhood_items
from main.utils import get_favorites, unslugify
from blog.models import Article
from flowreport.models import SchoolSearch
from property.models import Property, PropertyRoom, Amenity, PropertyLeaseType, \
                            PropertyLeaseStart, PropertyLeaseTerm, PropertyFavorite


def search(request, **kwargs):
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
        try:
            min_price = request.POST['minPrice']
        except:
            min_price = "0"

        try:
            max_price = request.POST['maxPrice']
        except:
            max_price = "5000"

        try:
            min_bath = request.POST['minBath']
        except:
            min_bath = "0"

        try:
            max_bath = request.POST['maxBath']
        except:
            max_bath = "10"

        try:
            min_bed = request.POST['minBed']
        except:
            min_bed = "0"

        try:
            max_bed = request.POST['maxBed']
        except:
            max_bed = "10"

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

    return render(request, 'searchcontent/search.html',
        {'lat':lat, 'long':long, 'school':school, 'url_prefix':'search',
        'modal_title':modal_title, 'properties':properties, 'favorited':favorited, 'rooms':rooms,
        'lease_types':lease_types, 'lease_terms':lease_terms, 'lease_starts':lease_starts,
        'special_amenities':special_amenities, 'google_api_key':settings.GOOGLE_API_KEY})


def group_info(request):
    # give basic info for what the search group is

    return render(request, "searchcontent/group.html", {})


@login_required
def create_group(request):
    '''
    create a new group and then be directed to the manage page
    to add other users
    '''
    template_name = "searchcontent/create_group.html"

    if request.method == "POST":
        form = GroupForm(request.POST)

        if form.is_valid():
            # save the group
            form.save()
            group = form.save()

            # save the current user into the group
            member = GroupMember(user=request.user, group=group)
            member.save()

            success_url = reverse('search-group-manage')

            return redirect(success_url)
        else:
            return render(request, template_name, {'form': form})
    else:
        form = GroupForm()


    return render(request, template_name,
        {'form': form})


@login_required
def view_group(request, pk):
    '''
    view the properties and comments that have been added into your group search
    have the ability to add, remove, edit comments as well as add/remove
    properties.
    '''

    group = get_object_or_404(Group, id=pk)
    members = GroupMember.objects.filter(group=group)
    properties = GroupProperty.objects.filter(group=group)
    # properties = []
    # for p in group_properties:
    #     properties.append(p.property)

    recent_comments = GroupComment.objects.filter(author__group=group)[:6]

    # determine if the user in the group
    try:
        member = GroupMember.objects.get(group=group, user=request.user)
    except:
        return render(request, "searchcontent/view_group.html",
            {'error': 'You do not have access to this group. Maybe you entered the id by mistake? ' +
                'Find your group through <a href="/search/group/manage/">Manage Groups</a>'})

    # get the users and then gather the favorites
    user_list = []
    for m in members:
        user_list.append(m.user)

    favorites = PropertyFavorite.objects.filter(user__in=user_list)

    if request.method == "POST":
        # save the comment that was posted
        comment = request.POST["comment"]
        property_id = request.POST["propertyId"]

        property = get_object_or_404(Property, id=property_id)
        user = User.objects.get(username=request.user.username)
        gp = get_object_or_404(GroupProperty, property=property, group=group)
        gm = GroupMember.objects.get(group=group, user=user)

        gc = GroupComment(group_property=gp, author=gm, text=comment)
        gc.save()

    return render(request, "searchcontent/view_group.html",
        {'group': group, 'properties': properties, 'members': members,
         'favorites': favorites, 'recent_comments': recent_comments})


@login_required
def manage_group(request):
    '''
    perform managerial tasks of the group. Some things might include leaving
    the group, adding new members, removing members (admin)
    '''

    # Show a list of groups that a user is in, and provide link and option to leave group
    user = request.user

    # list of groups that the user is a member of
    my_group_members = GroupMember.objects.filter(user=user)

    group_ids = []
    for m in my_group_members:
        group_id = m.group.id
        group_ids.append(group_id)

    groups = Group.objects.filter(id__in=group_ids)

    if request.method == "POST":
        # attempt to add the user into the selected group
        try:
            '''
            get the post variables. If they weren't supplied in the post then that
            means there was a problem with the post request
            '''
            username = request.POST['username']
            group_id = request.POST['group_id']
        except:
            error_msg = "There was a problem determining who you are trying to add/remove"
            return render(request, "searchcontent/manage_group.html",
                  {'groups': groups, 'error_msg': error_msg})

        if 'add' in request.POST:
            '''
            save the new member to the group. If this fails then that probably means
            the user entered the username to add incorrectly
            '''
            try:
                user = User.objects.get(username=username)
                group = Group.objects.get(id=group_id)
                gm = GroupMember(user=user, group=group)
                gm.save()
            except:
                error_msg = "There was a problem saving. Maybe their username is wrong?"
                return render(request, "searchcontent/manage_group.html",
                      {'groups': groups, 'error_msg': error_msg})

        elif 'remove' in request.POST:
            try:
                '''
                remove the user from a group
                '''
                user = User.objects.get(username=username)
                group = Group.objects.get(id=group_id)
                gm = GroupMember.objects.get(user=user, group=group)
                gm.delete()
            except Exception as e:
                error_msg = "There was a problem deleting the user. Not sure what's wrong, looking into it now."
                return render(request, "searchcontent/manage_group.html",
                      {'groups': groups, 'error_msg': e})


    return render(request, "searchcontent/manage_group.html",
                  {'groups': groups})
