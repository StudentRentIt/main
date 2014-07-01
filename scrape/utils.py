import re
import requests
from django.shortcuts import get_object_or_404
from django.utils.text import slugify

from main.models import City
from property.models import Property
from school.models import School
from scrape.models import Apartment, ApartmentImage, ApartmentAmenity, ApartmentFloorPlan, \
                            Source, Log

from bs4 import BeautifulSoup
from pygeocoder import Geocoder


def scrape_apartmentlist_data(city_obj):
    '''
    Scrape data from apartmentlist. For apartmentlist, they have multiple parent pages
    that show highlighted information for each apartment complex. We will go into
    each of those apartment pages and extract the data.
    '''

    #clear temporary apartment table
    Apartment.objects.all().delete()

    source = get_object_or_404(Source, id=1)
    base_url = source.link
    property_links = []
    pages = []

    #based on the school city and state, scrape data.
    city = slugify(city_obj.name)
    state = city_obj.state.lower()

    #get the parent page data for the given city
    url = base_url + state + "/" + city
    full_page  = requests.get(url).text
    soup = BeautifulSoup(full_page)

    '''
    get a list of all the parent pages. Add the page to our pages list variable
    and then if it has a Next link go to that page and then rinse and repeat. Many
    of apartmentlists listings are crap, so we're going to throw out anything that
    doesn't have an actual name (just the address as a placeholder)
    '''
    pages.append(url)
    page_numbers = []

    if soup.find("a", class_="medium secondary button"):
        for page in soup.findAll('a', class_="medium secondary button"):
            page_numbers.append(page['href'].split("?page=",1)[1])

        #get the max page and then generate the pages to scrape
        max_page = max(page_numbers)
        for x in range(2, int(max_page) + 1):
            pages.append(url + "?page=" + str(x))


    '''
    build up all the apartment links for the given city. For Apartmentlist, they
    can have multiple pages. Parse through all the pages for a city and then get
    a list of all the Property URLs to extract data.
    '''
    for page_url in pages:
        soup = BeautifulSoup(requests.get(page_url).text)

        for apt in soup.findAll('a', class_="listing"):
            property_links.append(base_url + apt['href'])

    '''
    Loop through property pages and temporarily store the apartment data. This is where we get
    the actual data for the individual apartment and save the temporary apartment object
    '''
    for p in property_links:
        url = p
        apt_page = requests.get(url).text
        soup = BeautifulSoup(apt_page)

        #collect all the required data
        try:
            title = soup.find(class_="listing-name").string
            address = soup("h2", class_="listing-location")[0].contents[0]
            city = soup.select(".listing-location a")[0].string.split(', ')[0]
            state = soup.select(".listing-location a")[0].string.split(', ')[1]
            location = Geocoder.geocode(address + ' ' + city + ', ' + state)
            lat = location[0].coordinates[0]
            long = location[0].coordinates[1]

            city_obj = City.objects.get(name=city)
            school = School.objects.get(city=city_obj)
        except:
            '''
            could not get all required data, go to next iteration. Not logging anymore
            because this happens a lot and it floods the log with useless data now that
            we know the title doesn't come through on the listings with address as name
            '''

            # try:
            #     title
            # except:
            #     title = "none"

            # instance = Log(city=city_obj, status="E", apartment_name=title, comment="Could not get required fields",
            #                 link=url)
            # instance.save()
            continue

        '''
        the following fields are not required. If we can't find the data,
        set them to null
        '''
        try:
            zip_cd = None #soup.find_all("h2")
        except:
            zip_cd = None

        try:
            phone = soup.find_all(class_="mobile-phone-link")[0].string
        except:
            phone = None

        try:
            description = ""
            desc = soup.find_all(class_="expansion-content")[0].stripped_strings
            for d in desc:
                if "ID: " not in d and "(RLNE" not in d:
                    description += d
        except:
            description = None

        #create the temp database object
        property_titles = []
        properties = Property.objects.all()
        for p in properties:
            property_titles.append(p.title)

        if title in property_titles:
            exists = True
        else:
            exists = False

        apt = Apartment(title=title, school=school, description=description,
                        address=address, phone=phone, zip_cd=zip_cd, source=source,
                        lat=lat, long=long, city=city, state=state, exists=exists)
        apt.save()

        #get apartment pics
        pics_all = soup.find(id="listing-carousel-inner").find_all('img')[0:6]

        for p in pics_all:
            instance = ApartmentImage(link = p['src'], apartment = apt)
            instance.save()

        #get apartment amenities
        amenities = soup.find_all(class_="amenity")

        for a in amenities:
            instance = ApartmentAmenity(title = a.string, apartment = apt)
            instance.save()

        #get apartment floorplans
        floor_plans = soup.find_all(class_="floorplan-unit")

        for f in floor_plans:
            split = f['data-summary'].split()

            '''
            if there is a studio, we need to replace change the first element to
            remove the first element and add 0, Bed to make the pattern match
            '''
            if split[0] == 'Studio,':
                del split[0]
                split = ['0', 'Bed'] + split

            try:
                bed_count = split[0]
                if bed_count == "Studio,":
                    bed_count = 0
            except:
                bed_count = 1

            try:
                bath_count = split[2]
                if not bath_count.isdecimal():
                    bath_count = 1
            except:
                bath_count = 1

            # sometimes the price is in position 5 if there is no sq ft provided
            if '$' in split[5]:
                try:
                    price = re.sub("[^0-9]", "", split[5])
                    if not price:
                        price = "987"
                    sq_ft = 0
                except:
                    sq_ft = 0
            else:
                try:
                    price = re.sub("[^0-9]", "", split[9])
                    #price = split[9].replace("$", "").replace(",", "")
                    if not price:
                        price = 0
                except:
                    price = 0

                try:
                    sq_ft = re.sub("[^0-9]", "", split[5])
                    #sq_ft = split[5].replace(",", "")
                    if not sq_ft:
                        sq_ft = 0
                except:
                    sq_ft = 0


            instance = ApartmentFloorPlan(bed_count=bed_count, bath_count=bath_count,
                                            sq_ft=sq_ft, price=price, apartment=apt)
            instance.save()

    # return a list of apartments that don't exist in our data
    apartments = Apartment.objects.filter(exists=False)

    return apartments


def scrape_myapartmentmap_data(request):

    return True
