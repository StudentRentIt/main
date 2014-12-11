from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView

from main import urls as mainurls
from main.utils import GenericSubdomainSitemap
from property.models import Property
from blog.models import Article
from school.models import School


admin.autodiscover()

#get dictionaries and build the sitemap
school_info_dict = {
    'queryset': School.objects.all(),
    'changefreq': 'monthly',
}
property_info_dict = {
    'queryset': Property.objects.all(),
    'changefreq': 'daily'
}
article_info_dict = {
    'queryset': Article.objects.all(),
    'changefreq': 'daily'
}
sitemaps = {
    "property": GenericSubdomainSitemap(property_info_dict, priority=1.0),
    "article": GenericSubdomainSitemap(article_info_dict, priority=0.8),
    "school": GenericSubdomainSitemap(school_info_dict, priority=0.6),
}


urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^property/', include('property.urls')),
    url(r'^school/', include('school.urls')),
    url(r'^scrape/', include('scrape.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^ca/', include('campusamb.urls')),
    url(r'^realestate/', include('realestate.urls')),
    url(r'^', include(mainurls)),

    #internal apps
    (r'^internal/reports/', include('flowreport.urls')),

    url(r'^robots\.txt', TemplateView.as_view(template_name="maincontent/robots.txt")),
    (r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemaps})
)