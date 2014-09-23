import math

from django.contrib.sitemaps import Sitemap
from django.contrib.sites.models import Site
from django.core.exceptions import ImproperlyConfigured

from property.models import PropertyFavorite
from flowreport.models import PropertyImpression, SchoolItemImpression


def get_favorites(user):
    '''
    used to get a list of properties that a user has favorited
    '''
    if user.is_authenticated():
        favorited = PropertyFavorite.objects.filter(user=user).values_list(
                                                                'property', flat=True)
    else:
        favorited = False

    return favorited


def save_impression(imp_type, imp_school_item_type=None,
                    imp_school_item_id=None, imp_property=None):
    '''
    Saves the impression. Right now we don't actually have a school impression so
    we are only saving property impressions.
    '''
    if imp_school_item_type:
        si = SchoolItemImpression
        si.item_type = imp_school_item_type
        si.item_id = imp_school_item_id
        si.imp_type = imp_type
        si.save()
    elif imp_property:
        pi = PropertyImpression()
        pi.imp_property_package = imp_property.package
        pi.imp_property_sponsored = imp_property.sponsored
        pi.imp_type = imp_type
        pi.property = imp_property
        pi.save()


class SubdomainSitemap(Sitemap):
    '''
    Redifine get_urls to add www to the link
    '''
    def __get(self, name, obj, default=None):
        try:
            attr = getattr(self, name)
        except AttributeError:
            return default
        if callable(attr):
            return attr(obj)
        return attr


    def get_urls(self, page=1, site=None, protocol=None):
        subdomain = 'www.'

        # Determine protocol
        if self.protocol is not None:
            protocol = self.protocol
        if protocol is None:
            protocol = 'http'

        # Determine domain
        if site is None:
            if Site._meta.installed:
                try:
                    site = Site.objects.get_current()
                except Site.DoesNotExist:
                    pass
            if site is None:
                raise ImproperlyConfigured("To use sitemaps, either enable the sites framework or pass a Site/RequestSite object in your view.")
        domain = site.domain

        urls = []
        for item in self.paginator.page(page).object_list:
            loc = "%s://%s%s%s" % (protocol, subdomain, domain, self.__get('location', item))
            priority = self.__get('priority', item, None)
            url_info = {
                'item':       item,
                'location':   loc,
                'lastmod':    self.__get('lastmod', item, None),
                'changefreq': self.__get('changefreq', item, None),
                'priority':   str(priority if priority is not None else ''),
            }
            urls.append(url_info)
        return urls


class GenericSubdomainSitemap(SubdomainSitemap):
    '''
    redifine generic site map to be based on the newly definted SubdomainSitemap
    Nothing changed in this from GenericSiteMap, just changed the base class
    '''

    priority = None
    changefreq = None

    def __init__(self, info_dict, priority=None, changefreq=None):
        self.queryset = info_dict['queryset']
        self.date_field = info_dict.get('date_field', None)
        self.priority = priority
        self.changefreq = changefreq

    def items(self):
        # Make sure to return a clone; we don't want premature evaluation.
        return self.queryset.filter()

    def lastmod(self, item):
        if self.date_field is not None:
            return getattr(item, self.date_field)
        return None


def distance(origin, destination):
    # using the haversine formula to get the distance
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 3959 # mi

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d


def unslugify(string):
    '''
    reverse the slugify function. replace hyphen with space and capitalize first letter
    of each word
    '''
    string = string.replace('-', ' ').title

    return string



