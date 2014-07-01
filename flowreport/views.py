import datetime
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.db.models import Count

from main.models import Contact
from property.models import PropertyReserve, Property, PropertySchedule
from flowreport.models import Report, SchoolSearch, PropertyImpression, SchoolItemImpression
from braces.views import StaffuserRequiredMixin


one_week_ago = datetime.date.today() - datetime.timedelta(days=7)

class ReportHomeListView(StaffuserRequiredMixin, ListView):
    '''
    displays the default report home dashboard
    '''
    model = Report
    template_name = "flowreport/content/home.html"

    def get_context_data(self, **kwargs):
        '''
        Get all the sets of data that will be displayed for the internal homepage
        '''
        context = super(ReportHomeListView, self).get_context_data(**kwargs)
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
        context['prop_imps'] = PropertyImpression.objects.values('imp_date') \
                    .filter(imp_date__gt=one_week_ago).annotate(created_count=Count('id'))

        #properties used for autocompleter
        context['properties'] = Property.objects.all()
        return context


class PropertySummaryListView(ListView):
    '''
    owner facing property summary report
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


class PropertyImpListView(StaffuserRequiredMixin, PropertySummaryListView):
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
                    .extra(select={'month': "EXTRACT(month FROM imp_date)"}) \
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