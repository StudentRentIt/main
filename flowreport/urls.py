from django.conf.urls import patterns, url

from flowreport.views import StaffReportListView, PropertyImpListView, \
    ImpTypeListView, save_impression, SchoolSearchSummaryListView, ImpTypeDailyListView, \
    SchoolSearchDetailListView, RealEstateListView

urlpatterns = patterns('',
    url(r'^$', StaffReportListView.as_view(), name='report-home'),
    url(r'realestate/(?P<slug>\S+)/$', RealEstateListView.as_view(), 
        name='report-real-estate-home'),

    url(r'property/(?P<pk>\d+)/$', PropertyImpListView.as_view(), name='report-prop-detail'),

    url(r'imptype/summary/$', ImpTypeListView.as_view(), name='report-imp-type-summary'),
    url(r'imptype/detail/$', ImpTypeDailyListView.as_view(), name='report-imp-type-detail'),

    url(r'schoolsearch/summary/$', SchoolSearchSummaryListView.as_view(),
        name='report-school-search-summary'),
    url(r'schoolsearch/detail/$', SchoolSearchDetailListView.as_view(),
        name='report-school-search-detail'),

    url(r'saveimpression/$', save_impression, name='save-impression'),
)