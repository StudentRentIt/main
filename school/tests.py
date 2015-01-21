from django.test import TestCase
from django.core.urlresolvers import reverse

from django_webtest import WebTest

from .urls import prefix
from test.factories import CityFactory, SchoolFactory, NormalUserFactory, NeighborhoodFactory, \
                           DealFactory, EventFactory, PropertyFactory
                           

class SchoolSetUp(object):
    def setUp(self):
        self.user = NormalUserFactory.create()
        self.city = CityFactory.create()
        self.school = SchoolFactory.create(city=self.city)
        self.neighborhood = NeighborhoodFactory.create(school=self.school)


class SchoolViewTest(SchoolSetUp, WebTest):
    def test_home(self):
        url = reverse(prefix + 'home')
        response = self.app.get(url)
        assert response.status_code == 200

    def test_neighborhood(self):
        url = self.neighborhood.get_absolute_url()
        response = self.app.get(url)
        assert response.status_code == 200

    def test_info(self):
        url = self.school.get_info_url()
        response = self.app.get(url)
        assert response.status_code == 200

    


