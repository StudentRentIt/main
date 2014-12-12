import datetime
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import TemplateView
#from django.views.generic.detail import DetailView, SingleObjectMixin
from django.http import HttpResponse
from django.db.models import Count, Sum

from main.models import Contact
from main.utils import unslugify
from property.models import PropertyReserve, Property, PropertySchedule
from flowreport.models import Report, SchoolSearch, PropertyImpression, SchoolItemImpression
from braces.views import StaffuserRequiredMixin
from realestate.models import Company
from realestate.utils import user_in_company

one_week_ago = datetime.date.today() - datetime.timedelta(days=7)

class BaseReportListView(ListView):
    '''
    displays the default report home dashboard
    '''
    model = Report
    template_name = "flowreport/content/home.html"

    def get_context_data(self, **kwargs):
        '''
        Get all the sets of data that will be displayed for the internal homepage
        '''
        context = super(BaseReportListView, self).get_context_data(**kwargs)
        context['admin'] = True
        context['contacts'] = Contact.objects.values('contact_date') \
                    .filter(contact_date__gt=one_week_ago).annotate(created_count=Count('id')) \
                    .order_by('-contact_date')
        context['reservations'] = PropertyReserve.objects.values('reserve_date') \
                    .filter(reserve_date__gt=one_week_ago).annotate(created_count=Count('id'))
        context['schedules'] = PropertySchedule.objects.values('create_date') \
                    .filter(create_date__gt=one_week_ago).annotate(created_count=Count('id'))
        context['school_searches'] = SchoolSearch.objects.values('search_date') \
                    .filter(search_date__gt=one_week_ago).annotate(created_count=Count('id')) \
                    .order_by('-search_date')
        prop_imps = PropertyImpression.objects.filter(imp_date__gt=one_week_ago)\
                    .values('imp_date') \
                    .annotate(created_count=Count('id'))


        context['prop_imps'] = prop_imps

        #properties used for autocompleter
        context['properties'] = Property.objects.all()
        return context

class StaffReportListView(StaffuserRequiredMixin, BaseReportListView):

    def get_context_data(self, **kwargs):
        '''
        let the template know that it is an admin/staff user
        '''
        context = super(BaseReportListView, self).get_context_data(**kwargs)
        context['admin'] = True

class RealEstateListView(BaseReportListView):

    def get_context_data(self, **kwargs):
        '''
        Get all the set of data that is viewable by real estate company employees. We need to
        filter the existing context variables from BaseReportListView by the real estate company.
        We also need to set some variables to be used in the template.
        '''
        name_slug = self.kwargs['slug']
        company = get_object_or_404(Company, name=unslugify(name_slug))

        context = super(RealEstateListView, self).get_context_data(**kwargs)

        # check if user is in company. If not, don't return any data
        if user_in_company(self.request.user, company):
            context['schedules'] = context['schedules'].filter(property__real_estate_company=company)
            context['prop_imps'] = context['prop_imps'].filter(property__real_estate_company=company)
            
            #properties used for autocompleter
            context['properties'] = context['properties'].filter(real_estate_company=company)
        else:
            # return no data for the sensitive data
            context['schedules'] = PropertySchedule.objects.none()
            context['prop_imps'] = PropertyImpression.objects.none()
            context['properties'] = Property.objects.none()

            # pass a variable to tell the user they don't have access
            context['error'] = "access_error"

        context['real_estate_company'] = company
        context['admin'] = False

        return context


class PropertySummaryListView(ListView):
    '''
    owner and real-estate facing property summary report
    '''
    template_name = "flowreport/content/reports/property_imp_detail.html"
    report_view = "owner"

    def get_context_data(self, **kwargs):
        context = super(PropertySummaryListView, self).get_context_data(**kwargs)
        property = get_object_or_404(Property, id=self.kwargs['pk'])
        context['object'] = property
        context['report_view'] = self.report_view
        #get an impression count by month
        context['imps_by_month'] = PropertyImpression.objects \
                .extra(select={'month': "EXTRACT(month FROM imp_date)"}) \
                .filter(property=property, property__user=self.request.user) \
                .values('month') \
                .annotate(created_count=Count('id')) \
                .order_by('month')
        return context

    def get_queryset(self):
        property = get_object_or_404(Property, id=self.kwargs['pk'])
        qs = PropertyImpression.objects.values('imp_date') \
                                        .filter(property=property, property__user=self.request.user) \
                                        .annotate(created_count=Count('id'))
        return qs


class PropertyImpListView(PropertySummaryListView):
    '''
    admin version of the Property Summary report
    '''
    report_view = "admin"

    def get_queryset(self):
        property = get_object_or_404(Property, id=self.kwargs['pk'])
        qs = PropertyImpression.objects.values('imp_date') \
                    .filter(property=property, imp_date__gt=one_week_ago) \
                    .annotate(created_count=Count('id'))
        return qs

    def get_context_data(self, **kwargs):
        context = super(PropertyImpListView, self).get_context_data(**kwargs)
        property = get_object_or_404(Property, id=self.kwargs['pk'])

        #properties used for autocompleter
        context['properties'] = Property.objects.all()

        #get an impression count by month
        context['imps_by_month'] = PropertyImpression.objects \
                    .extra(select={'month': "extract(month FROM imp_date)"}) \
                    .filter(property=property) \
                    .values('month') \
                    .annotate(created_count=Count('id')) \
                    .order_by('month')
        return context


class SchoolSearchSummaryListView(StaffuserRequiredMixin, TemplateView):

    template_name = "flowreport/content/reports/school_search_summary.html"

    def get_context_data(self, **kwargs):
        context = super(SchoolSearchSummaryListView, self).get_context_data(**kwargs)
        context['search_by_school'] = SchoolSearch.objects.values('school__name') \
                    .annotate(created_count=Count('id')) \
                    .order_by('-created_count')

        return context


class ImpTypeListView(StaffuserRequiredMixin, ListView):

    queryset = PropertyImpression.objects.values('imp_type').annotate(created_count=Count('id'))
    template_name = "flowreport/content/reports/imp_type_summary.html"


def save_impression(request):
    '''
    passed in as a json object to register all types of impressions. There are
    different impression classes which are stored in different models. Impression is when we
    consider the users have seen a property or school item and we use this to
    report back to the property or business owners.
    '''
    if request.is_ajax():
        if request.method == 'POST':
            imp_class = request.POST['impClass']
            imp_type = request.POST['impType']

            if imp_class == "property":
                property = Property.objects.get(id=request.POST['propertyId'])
                pi = PropertyImpression()
                pi.imp_type = imp_type
                pi.property = property
                pi.save()
                return HttpResponse("Impression saved for " + property.title)
            elif imp_class == "schoolItem":
                si = SchoolItemImpression()
                si.item_type = request.POST['schoolItemType']
                si.item_id = request.POST['schoolItemId']
                si.imp_type = imp_type
                si.save()
                return HttpResponse("Impression saved for school item")
            else:
                return HttpResponse("Impression Class Invalid")
    else:
        return HttpResponse("Request not AJAX nor POST")


class ImpTypeDailyListView(StaffuserRequiredMixin, ListView):
    '''
    show the daily breakout of impression types
    '''
    queryset = PropertyImpression.objects.values('imp_date', 'imp_type').annotate(created_count=Count('id'))
    template_name = "flowreport/content/reports/imp_type_summary_daily.html"


class SchoolSearchDetailListView(StaffuserRequiredMixin, ListView):
    template_name = "flowreport/content/reports/school_search_detail.html"
    queryset = SchoolSearch.objects.values('search_date', 'school__name') \
                    .annotate(created_count=Count('id')).order_by('-search_date')