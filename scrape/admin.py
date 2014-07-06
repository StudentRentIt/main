from django.contrib import admin

from scrape.models import Apartment, Source, AmenityCrossWalk

admin.site.register(AmenityCrossWalk)
admin.site.register(Apartment)
admin.site.register(Source)