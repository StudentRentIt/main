import requests

from django.shortcuts import render, get_object_or_404
from django.utils.text import slugify

from main.models import School, City
from scrape.models import Apartment, ApartmentPic, ApartmentAmenity, ApartmentFloorPlan

from bs4 import BeautifulSoup


def apartment_list_data(request):
    #Clean up Apartment table, we are using this as a temporary data table
    Apartment.objects.all().delete()

    '''
    scrape data from apartmentlist.com
    '''
    template_name = "scrapecontent/home.html"
    base_url = "http://www.apartmentlist.com"
    property_links = []
    pages = []
    schools = School.objects.filter(id=3)

    for s in schools:
        #based on the school city and state, scrape data.
        city = slugify(s.city.name.lower())
        state = s.city.state.lower()

        #get the page data for the given city
        url = base_url + "/" + state + "/" + city
        full_page  = requests.get(url).text
        soup = BeautifulSoup(full_page)

        '''
        get a list of all the parent pages. Add the page to our pages list variable
        and then if it has a Next link go to that page and then rinse and repeat.
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
            for apt in soup.findAll('a', class_="listing"):
                property_links.append(base_url + apt['href'])

    '''
    Loop through property pages and store the apartment data
    '''
    for p in property_links[25:29]:
        url = p
        apt_page = requests.get(url).text
        soup = BeautifulSoup(apt_page)

        #collect all the data
        try:
            name = soup.find(class_="listing-name").string
        except:
            name = None

        try:
            address = soup("h2", class_="listing-location")[0].contents[0]
        except:
            address = None

        try:
            zip_cd = None #soup.find_all("h2")
        except:
            zip_cd = None

        try:
            phone = soup.find_all(class_="mobile-phone-link")[0].string
        except:
            phone = None

        try:
            city = soup.select(".listing-location a")[0].string.split(', ')[0]
            city_obj = City.objects.get(name=city)
            school = School.objects.get(city=city_obj)
        except:
            school = None

        try:
            description = ""
            desc = soup.find_all(class_="expansion-content")[0].stripped_strings
            for d in desc:
                if "ID: " not in d and "(RLNE" not in d:
                    description += d
        except:
            description = None

        #create the database object
        apt = Apartment(name=name, school=school, description=description,
                        address=address, phone=phone, zip_cd=zip_cd, source='A',
                        source_link=p)
        apt.save()

        #get apartment pics
        pics_all = soup.find(id="listing-carousel-inner").find_all('img')[0:6]

        for p in pics_all:
            instance = ApartmentPic(link = p['src'], apartment = apt)
            instance.save()

        #get apartment amenities
        amenities = []
        amenities_all = soup.find_all(class_="amenity")

        for a in amenities_all:
            # amenities.append(a.string)
            instance = ApartmentAmenity(title = a.string, apartment = apt)
            instance.save()

        #get apartment floorplans
        floor_plans = []
        floor_plans_all = soup.find_all(class_="floorplan-unit")

        for f in floor_plans_all:
            split = f['data-summary'].split()

            try:
                bed_count = split[0]
            except:
                bed_count = None

            try:
                bath_count = split[2]
            except:
                bath_count = None

            # sometimes the price is in position 5 if there is no sq ft provided
            if '$' in split[5]:
                try:
                    price = split[5].replace("$", "").replace(",", "")
                    sq_ft = None
                except:
                    sq_ft = None
            else:
                try:
                    price = split[9].replace("$", "").replace(",", "")
                except:
                    price = None

                try:
                    sq_ft = split[5].replace(",", "")
                except:
                    sq_ft = None


            instance = ApartmentFloorPlan(bed_count=bed_count, bath_count=bath_count,
                                            sq_ft=sq_ft, price=price, apartment=apt)
            instance.save()

    apartments = Apartment.objects.all()

    return render(request, template_name,
        {'links':property_links, 'pages':pages, 'apartments':apartments,
        'amenities':amenities, 'floor_plans':floor_plans})

