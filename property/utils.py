import requests

from django.conf import settings


def get_place_data(p):
    # get variables needed to build up the api calls
    property_search_prefix = "https://maps.googleapis.com/maps/api/place/nearbysearch/"
    data_type = "json"

    # build and execute property search api call
    url = property_search_prefix + data_type + '?location=' + str(p.lat) + ',' + str(p.long) + \
                                 '&name=' + p.title + '&radius=100&key=' + settings.GOOGLE_API_KEY
    data = requests.get(url).json()

    return data

# @staff_member_required
# def get_place_ids(request):
#     # get the google place ids for all properties
#     template_name = "scrapecontent/reviews.html"
#     updated_properties = []
#
#     properties = Property.objects.filter(place_id=None)
#     for p in properties:
#         place_id = get_place_id(p)
#         if place_id:
#             # if we returned a place_id, store the place_id for the property
#             p.place_id = place_id
#             p.save()
#
#             # add to an updated list so that we can see what was updated
#             updated_properties.append(p)
#
#     return render(request, template_name, {'updated':updated_properties})
#
#
# def save_property_reviews(p):
#     # save property reviews based on the place_id
#     property_search_prefix = "https://maps.googleapis.com/maps/api/place/details/"
#     data_type = "json"
#     reviews = ""
#
#     #build property search api calls
#     url = property_search_prefix + data_type + '?placeid=' + p.place_id + '&key=' + settings.GOOGLE_API_KEY
#     r = requests.get(url).json()
#     status = r.get('status')
#
#     if status == 'OK':
#         if r.get('result').get('reviews'):
#             # loop through the reviews and save them to the database
#             reviews = r.get('result').get('reviews')
#
#             for r in reviews:
#                 # save the review
#                 PropertyReview(rating=r.get('rating'),
#                                time=r.get('time'),
#                                text=r.get('text'),
#                                author_name=r.get('author_name'),
#                                author_url=r.get('author_url'))
#                 review_list.append(p)
#
#             return p
#
#     return None
#
#
# @staff_member_required
# def reviews(request):
#     # home page to view an overview of the review functionality
#     template_name = "scrapecontent/reviews.html"
#
#     return render(request, template_name, {})
#
#
# @staff_member_required
# def get_reviews(request, **kwargs):
#     # get the reviews for a set of properties
#     template_name = "scrapecontent/reviews.html"
#     properties = Property.objects.filter(place_id__isnull=False)
#     reviews = []
#
#     for p in properties:
#         reviews.append(save_property_reviews(p))
#
#     return render(request, template_name, {'properties':properties, 'reviews':reviews})
#
#
# @staff_member_required
# def reviews_property(request, **kwargs):
#     # view and get the new reviews for a property
#     template_name = "scrapecontent/reviews.html"
#     p = get_object_or_404(Property, id=kwargs['pk'])
#
#     save_property_reviews(p)
#     if save_property_reviews(p):
#         saved = p
#
#     return render(request, template_name, {'saved':saved})