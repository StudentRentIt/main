from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.core.urlresolvers import reverse

from django_webtest import WebTest

from test.factories import NormalUserFactory, CityFactory, SchoolFactory, CompanyFactory, \
                           PropertyFactory, ArticleFactory, TagFactory


class BlogSetUp(TestCase):
    def setUp(self):
        # set up required model instances
        self.user = NormalUserFactory.create()
        self.city = CityFactory.create()
        self.school = SchoolFactory.create(city=self.city)
        self.company = CompanyFactory.create(default_school=self.school)
        self.property = PropertyFactory.create(school=self.school, user=self.user, 
            real_estate_company=self.company)

        # set up the school models
        self.tag1 = TagFactory.create(tag_name="Tag 1")
        self.tag2 = TagFactory.create(tag_name="Tag 2")
        self.article = ArticleFactory.create(
            user=self.user, 
            school=self.school, 
            property=self.property
        )
        self.article.tags.add(self.tag1, self.tag2)


class ViewTests(BlogSetUp, WebTest):
    def test_home(self):
        url = reverse('blog-home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_article(self):
        url = self.article.get_absolute_url()
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    def test_type_school(self):
        # test the type view when passing in a school
        url = reverse('blog-type', kwargs={'pk':'1' , 'slug':'test-article', 'type':'school'})
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

    def test_type_property(self):
        # test the type view when passing in a property
        url = reverse('blog-type', kwargs={'pk':'1' , 'slug':'test-article', 'type':'property'})
        response = self.app.get(url)
        self.assertEqual(response.status_code, 200)

