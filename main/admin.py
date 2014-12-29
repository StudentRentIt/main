from django.contrib import admin
#from django.contrib.auth import get_user_model
#from django.contrib.auth.admin import UserAdmin

from main.models import City, Payment, TeamMember, User
from school.models import School, Event, Deal, Neighborhood
from blog.models import Article, Tag
from property.models import Property, PropertyImage, PropertyRoom, PropertyFavorite, \
                            PropertyLeaseTerm, PropertyLeaseType, PropertyLeaseStart, \
                            PropertyReserve, Package, Service, Amenity, PropertyVideo
from search.models import GroupProperty, GroupComment
from realestate.models import Company


# we define our resources to add to admin pages to use a RTE
class CommonMedia:
  js = (
    'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
    '/static/js/plugins/dojo-editor.js',
  )
  css = {
    'all': ('/static/css/dojo-editor.css',),
  }

#allow extension of the user in admin


class PropertyImageInline(admin.StackedInline):
    model = PropertyImage


class PropertyRoomInline(admin.StackedInline):
    model = PropertyRoom


class PropertyVideoInline(admin.StackedInline):
    model = PropertyVideo


class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline, PropertyRoomInline, PropertyVideoInline, ]

admin.site.register(School)
admin.site.register(User)
admin.site.register(Neighborhood)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Amenity)
admin.site.register(PropertyFavorite)
admin.site.register(PropertyLeaseType)
admin.site.register(PropertyLeaseTerm)
admin.site.register(PropertyLeaseStart)
admin.site.register(PropertyReserve)
admin.site.register(City)
admin.site.register(Tag)
admin.site.register(Package)
admin.site.register(Service)
admin.site.register(Payment)
admin.site.register(Article)
admin.site.register(TeamMember)
admin.site.register(Deal, Media = CommonMedia,)
admin.site.register(Event, Media = CommonMedia,)
admin.site.register(GroupProperty)
admin.site.register(GroupComment)
admin.site.register(Company)