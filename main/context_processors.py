from school.models import School, Deal, Roommate, Event
from property.models import Property
from blog.models import Article
from main.models import City

def all_schools(request):
    schools = School.objects.all()
    return {
        'schools':schools,
    }

def all_cities(request):
    '''
    used for the header section to hide Update School Ino if the user
    does not have any school info objects
    '''
    cities = City.objects.all()
    return {
        'cities':cities,
    }


def get_user_items(request):
    '''
    used for the header section to hide Update Properties and/or Update School
    Items. Get if the user has certain items and pass it through the context
    '''
    if request.user.is_authenticated():
        my_properties = Property.objects.filter(user=request.user)
        if my_properties:
            has_properties = True
        else:
            has_properties = False

        my_articles = Article.objects.filter(user=request.user)
        if my_articles:
            has_articles = True
        else:
            has_articles = False

        my_events = Event.objects.filter(user=request.user)
        if my_events:
            has_events = True
        else:
            has_events = False

        my_deals = Deal.objects.filter(user=request.user)
        if my_deals:
            has_deals = True
        else:
            has_deals = False

        my_roommates = Roommate.objects.filter(user=request.user)
        if my_roommates:
            has_roommates =True
        else:
            has_roommates = False

        if has_articles or has_events or has_deals or has_roommates:
            has_school_items = True
        else:
            has_school_items = False

        return {'has_properties': has_properties, 'has_articles':has_articles,
                'has_events':has_events, 'has_roommates':has_roommates, 'has_deals':has_deals,
                'has_school_items':has_school_items}
    return {}