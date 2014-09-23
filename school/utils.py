from django.shortcuts import get_object_or_404

from school.models import School, Event
from main.utils import unslugify
from blog.models import Article


def get_school(slug):
    '''
    pass in value to return the correct school object
    '''
    school = get_object_or_404(School, name__contains=unslugify(slug))

    return school


def item_dict(item):
    # shared function for building parameters to be used in get_school_items
    if item.image:
        image_url = item.image.url
    else:
        image_url = ""

    try:
        property = item.property
    except AttributeError:
        property = ""

    try:
        long = item.property.long
    except AttributeError:
        long = ""

    item = {'create_date':item.create_date,
            'title':item.title,
            'image_url':image_url,
            'content':item.heading,
            'property':item.property,
    }

    return item


def get_school_items(type, school):
    '''
    return the items that we want to show on the sidebar of the school and
    neighborhood community info pages.
    '''

    if type == "info":
        # get data for an entire school
        items = []
        articles = Article.objects.filter(school=school)[:4]
        events = Event.objects.filter(school=school)[:4]

        for a in articles:
            # build the article item and add it to the item list
            item = item_dict(a)
            item['type'] = 'article'
            items.append(item)

        for e in events:
            # build event items to add to the dictionary
            item = item_dict(e)
            item['type'] = 'event'
            items.append(item)

        return items

    elif type == "neighborhood":
        # get data for a neighborhood
        items = []

        return items