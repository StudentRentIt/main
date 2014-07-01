from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse

from main.models import City
from scrape.utils import scrape_apartmentlist_data
from scrape.models import Log, Apartment, AmenityCrossWalk
from property.models import Property, PropertyImage, PropertyRoom


@staff_member_required
def history(request):
    '''
    shows the history of changes that people have made to our property data.
    Will show additions, changes, and deletions
    '''
    history = Log.objects.all()[:100]
    template_name = "scrapecontent/history.html"

    return render(request, template_name,
        {'history':history})


@staff_member_required
def admin(request, **kwargs):
    '''
    this is where we sort through the scraped data and decide what we want to add
    or change. Will choose which source and city to choose from.
    '''
    all_cities = City.objects.all()
    template_name = "scrapecontent/admin.html"

    if 'city' in kwargs:
        '''
        for now we are going to just use one source, but in the future we might
        implement more and will call different functions for different sources, which
        should be passed in as a kwarg similar to city
        '''
        city = get_object_or_404(City, id=kwargs['city'])
        apartments = scrape_apartmentlist_data(city)
        # apartments = apartment_data[0]
        # property_links = apartment_data[1]
        # pages = apartment_data[2]
    else:
        apartments = None
        city = None
        # property_links = None
        # pages = None

    return render(request, template_name,
        {'all_cities':all_cities, 'city':city, 'apartments':apartments})


@staff_member_required
def add_property(request, pk):
    # add property from our temporary scrape data into permanent Property data
    if request.is_ajax():
        if request.method == 'POST':
            # assign property variables from the posted property
            p = get_object_or_404(Apartment, id=pk)


            # build a list of all amenity titles
            cw = AmenityCrossWalk.objects.all()
            amenity_titles = []

            for a in cw:
                amenity_titles.append(a.scrape_title)


            try:
                #save apartment and its related models
                images = p.apartmentimage_set.all()
                floor_plans = p.apartmentfloorplan_set.all()
                amenities = p.apartmentamenity_set.all()

                prop_instance = Property(title=p.title, addr=p.address, school=p.school,
                                    city=p.city, state=p.state, zip_cd=p.zip_cd, user=request.user,
                                    lat=p.lat, long=p.long, description=p.description)
                prop_instance.save()

                for a in amenities:
                    # get the permanent amenity based on crosswalk with scraped title
                    if a.title in amenity_titles:
                        amenity_xw = AmenityCrossWalk.objects.get(scrape_title=a.title)
                        prop_instance.amenities.add(amenity_xw.amenity)

                for i in images:
                    instance = PropertyImage(image_link=i.link, property=prop_instance, caption="")
                    instance.save()

                for f in floor_plans:
                    instance = PropertyRoom(property=prop_instance, price=f.price,
                        bed_count=f.bed_count, bath_count=f.bath_count, sq_ft=f.sq_ft)
                    instance.save()

                # log success
                instance = Log(city=p.school.city, apartment_name=p.title, status='S',
                            comment="Successfully saved " + p.title)
                instance.save()

                return HttpResponse("Successfully added " + p.title)
            except Exception as e:
                return HttpResponse(e)
        else:
            return HttpResponse("Not a POST request")
    else:
        return HttpResponse("Not an AJAX call")
