from django.contrib import admin

from scrape.models import Apartment, ApartmentPic, ApartmentAmenity, ApartmentFloorPlan

admin.site.register(Apartment)
admin.site.register(ApartmentPic)
admin.site.register(ApartmentAmenity)
admin.site.register(ApartmentFloorPlan)