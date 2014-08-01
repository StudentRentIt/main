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

def get_walkscore(p):
    # get the walkscore response for the property
    walkscore_api_key = settings.WALKSCORE_API_KEY
    url = "http://api.walkscore.com/score?format=json&address=" + str(p.addr) + "&lat=" + str(p.lat) + \
            "&lon=" + str(p.long) + "&wsapikey=" + walkscore_api_key

    data = requests.get(url).json()

    return data