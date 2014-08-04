import stripe
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.sitemaps import Sitemap
from django.views.generic import FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.conf import settings

from school.models import School
from property.models import Property, PropertyRoom, PropertyLeaseType, PropertyLeaseStart, \
                            PropertyLeaseTerm, Amenity, Service
from blog.models import Article
from main.models import Payment, TeamMember
from main.forms import ContactForm, UserUpdateForm
from main.utils import get_favorites

from flowreport.models import SchoolSearch

from braces.views import LoginRequiredMixin


class FormValidateMixin(object):

    def form_invalid(self, form, **kwargs):
        #need to add in the error status to the context_data
        context = self.get_context_data(**kwargs)
        context['status'] = 'error'
        context['form'] = form
        return self.render_to_response(context)

    def form_valid(self, form, **kwargs):
        #need to add in the saved status to the context_data
        context = self.get_context_data(**kwargs)
        context['status'] = 'saved'
        context['form'] = form

        form.instance.save()
        return self.render_to_response(context)


class PropertySiteMap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Property.objects.filter()

    def lastmod(self, obj):
        return obj.pub_date


#home page that people come to
class HomeListView(ListView):

    model = School
    template_name = "maincontent/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['url_prefix'] = 'search'
        return context


class ArticleListView(ListView):
    '''
    SchoolArticleListView inhertis from this view
    shows list views of general blogs
    '''

    model = Article
    template_name = "maincontent/blog/home.html"

    def get_queryset(self):
        objects = Article.objects.filter(general_page=True)
        return objects


class ArticleDetailView(DetailView):
    '''
    show an individual article in the school section
    '''

    model = Article
    template_name = "maincontent/blog/article.html"

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        '''
        get the next and previous articles to display in the article footer
        '''
        object_id = get_object_or_404(Article, id=kwargs['object'].id).id
        previous_article = Article.objects.filter(general_page=True, id__lt=object_id)
        next_article = Article.objects.filter(general_page=True, id__gt=object_id)

        try:
            context['author'] = TeamMember.objects.get(user=kwargs['object'].user)
        except:
            pass

        try:
            previous_id = previous_article[0].id
            context['previous_article'] = get_object_or_404(Article, id=previous_id)
        except:
            context['previous_article'] = None

        try:
            next_id = next_article.reverse()[0].id
            context['next_article'] = get_object_or_404(Article, id=next_id)
        except:
            context['next_article'] = None

        return context


def search(request, pk=None, slug=None):
    '''
    the page that allows people to search in depth for properties
    '''
    modal_title = "Find Housing, Apartments, Subleases and Information"
    properties = Property.objects.filter(school=pk, lat__isnull=False, long__isnull=False)
    rooms = PropertyRoom.objects.filter(property__in=properties).exclude(lease_start=3) #available
    favorited = get_favorites(request.user)

    min_price = None
    min_bed = None

    #save the search for metrics
    if pk:
        school = get_object_or_404(School, id=pk)
        search = SchoolSearch()
        search.school = school
        search.save()

    special_amenities = Amenity.objects.filter(special=True)

    #if the request is a POST, filter the properties. If not, show all properties for the school.
    if request.method == "POST":
        '''
        gather the post data filters. There are a couple different types of ways
        we gather the post data. The first is through normal text input which gives
        us a single value for the post data. Another way is through a list of values
        which is passed in by the user choosing multiple values
        '''

        if 'home-search' in request.POST:
            # search comes from the home page and will only include the couple search criteria
            beds = request.POST['beds']
            max_price = request.POST['maxPrice']

            if not max_price:
                max_price = 2000

            if beds:
                rooms = rooms.filter(price__lte=max_price, bed_count=beds)
            else:
                rooms = rooms.filter(price__lte=max_price)

        else:
            # search from the main search page

            #take the post data and create variables
            min_price = request.POST['minPrice']
            max_price = request.POST['maxPrice']
            min_bath = request.POST['minBath']
            max_bath = request.POST['maxBath']
            min_bed = request.POST['minBed']
            max_bed = request.POST['maxBed']
            distance = request.POST['distance']

            '''
            filter rooms based on post filters. We'll get a list of rooms and then
            filter the properties based on which rooms we have
            '''
            if min_price:
                rooms = rooms.filter(price__gte=min_price)

            if max_price:
                rooms = rooms.filter(price__lte=max_price)

            if min_bath:
                rooms = rooms.filter(bath_count__gte=min_bath)

            if max_bath:
                rooms = rooms.filter(bath_count__lte=max_bath)

            if min_bed:
                rooms = rooms.filter(bed_count__gte=min_bed)

            if max_bed:
                rooms = rooms.filter(bed_count__lte=max_bed)

            # if distance:
            #     #TODO after we put distance from campus as an attribute for properties
            #     rooms = rooms



        #create list of properties that are filtered
        property_filtered_list = []
        for r in rooms:
            property_filtered_list.append(r.property.id)

        #filter properties and add in businesses
        properties = properties.filter(id__in=property_filtered_list)
        businesses = Property.objects.filter(school=pk, type="BUS")
        properties = properties | businesses

    apartments = properties.exclude(type="BUS")

    #if location passed in, get the coordinates to center map
    if pk:
        school = get_object_or_404(School, id=pk)
        lat = school.lat
        long = school.long
    else: # default to Texas State, for now
        lat = 29.87
        long = -97.93
        school = None

    return render(request, 'maincontent/search.html',
        {'lat':lat, 'long':long, 'school':school, 'url_prefix':'search',
        'modal_title':modal_title, 'properties':properties, 'favorited':favorited, 'rooms':rooms,
        'special_amenities':special_amenities, 'apartments':apartments, 'min_price':min_price,
        'min_bed':min_bed})


class ContactView(FormView, FormValidateMixin):

    template_name = 'maincontent/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact-view')

    def form_invalid(self, form, **kwargs):
        #need to add in the error status to the context_data
        context = self.get_context_data(**kwargs)
        context['status'] = 'error'
        context['form'] = form
        return self.render_to_response(context)

    def form_valid(self, form, **kwargs):
        cd = form.cleaned_data
        send_mail(
            cd['subject'],
            cd['body'] + '  Reply To: ' + cd['email'],
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER])

        #need to add in the saved status to the context_data
        context = self.get_context_data(**kwargs)
        context['status'] = 'sent'
        context['form'] = form

        form.instance.save()
        return self.render_to_response(context)


class ProfileUpdateView(LoginRequiredMixin, FormValidateMixin, UpdateView):

    model = User
    form_class = UserUpdateForm
    template_name = 'maincontent/profile.html'
    success_url = '/accounts/profile/'

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        context['form_title_text'] = 'Update Profile'
        return context

    def get_object(self):
        return get_object_or_404(User, username=self.request.user)


def onetime_payment(request):

    if request.method == "POST":

        # Set your secret key: remember to change this to your live secret key in production
        # See your keys here https://manage.stripe.com/account
        stripe.api_key = settings.STRIPE_SECRET_KEY

        # Get the credit card details submitted by the form
        token = request.POST['stripeToken']
        amount = request.POST['amount']
        payment_type = request.POST['payment-type']

        if payment_type == "service":
            services_string = request.POST['services']
            property_id = request.POST['property']
            property = get_object_or_404(Property, id=property_id)

            services_list = services_string.split(", ")
            services=[]
            for s_id in services_list:
                service = get_object_or_404(Service, id=s_id)
                services.append(service)

            # Create the charge on Stripe's servers - this will charge the user's card
            try:
              charge = stripe.Charge.create(
                  amount=amount,
                  currency="usd",
                  card=token,
                  description="payinguser@example.com"
              )
              status = "accepted"
            except stripe.CardError as e:
              # The card has been declined
              status = "declined"

            #save in database
            payment = Payment()
            payment.user = request.user
            payment.property = property
            payment.amount = int(amount) / 100
            payment.save()

            payment.services = services
            payment.save()

            return render(request, 'maincontent/payments/payment.html',
                {'token':token, 'status':status, 'services':services, 'property':property})
        else:
            return HttpResponse("Payment type not recognized")
    else:
        return HttpResponse("Not a POST request")


def property_list(request, **kwargs):
    school = get_object_or_404(School, id=kwargs['pk'])
    apartments = Property.objects.filter(type="APT", school=school)
    businesses = Property.objects.filter(type="BUS", school=school)

    return render(request, "maincontent/property_list.html",
        {'apartments':apartments, 'businesses':businesses, 'school':school})
