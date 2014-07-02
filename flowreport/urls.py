from django.conf.urls import patterns, url

from flowreport.views import ReportHomeListView, PropertyImpListView, \
    ImpTypeListView, save_impression, SchoolSearchSummaryListView, ImpTypeDailyListView, \
    SchoolSearchDetailListView

urlpatterns = patterns('',
    url(r'^$', ReportHomeListView.as_view(), name='report-home'),

    url(r'property/(?P<pk>\d+)/$', PropertyImpListView.as_view(), name='report-prop-detail'),

    url(r'imptype/summary/$', ImpTypeListView.as_view(), name='report-imp-type-summary'),
    url(r'imptype/detail/$', ImpTypeDailyListView.as_view(), name='report-imp-type-detail'),

    url(r'schoolsearch/summary/$', SchoolSearchSummaryListView.as_view(),
        name='report-school-search-summary'),
    url(r'schoolsearch/detail/$', SchoolSearchDetailListView.as_view(),
        name='report-school-search-detail'),

    url(r'saveimpression/$', save_impression, name='save-impression'),
)