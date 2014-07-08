from django.utils import unittest
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.core.urlresolvers import reverse

from main.models import City
from property.models import Property
from school.models import School
from blog.models import Tag, Article


class ModelTests(unittest.TestCase):

    def setUp(self):
        # set up required model instances
        self.city = City.objects.create(name="Blog Test Town", state="TX")
        self.user = User.objects.create_user('blogtester', 'blogtester@somewhere.com', 'testpassword')
        self.school = School.objects.create(city=self.city, name="Blog Test University",
                        long=-97.1234123, lat=45.7801234)
        self.property = Property.objects.create(school=self.school, user=self.user, title="test property",
                        addr="13 Test St.", city="Test Town", state="TX")

        # set up the school models
        self.tag1 = Tag.objects.create(tag_name="Tag 1")
        self.tag2 = Tag.objects.create(tag_name="Tag 2")
        self.article = Article.objects.create(user=self.user, school=self.school, property=self.property,
                    title="Test Article", body="This is the body of the article.")
        self.article.tags.add(self.tag1, self.tag2)

    def test_models(self):
        Tag.objects.get(id=1)
        Article.objects.get(id=1)


class ViewTests(TestCase):

    def setUp(self):
        self.client = Client()

        # set up required model instances
        self.city = City.objects.create(name="Blog Test Town", state="TX")
        self.user = User.objects.create_user('blogtester', 'blogtester@somewhere.com', 'testpassword')
        self.school = School.objects.create(city=self.city, name="Blog Test University",
                        long=-97.1234123, lat=45.7801234)
        self.property = Property.objects.create(school=self.school, user=self.user, title="test property",
                        addr="13 Test St.", city="Test Town", state="TX")

        # set up the article instance
        Article.objects.create(user=self.user, title="Test Article",
                    body="This is the body of the article.")

    def test_home(self):
        url = reverse('blog-home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_article(self):
        url = reverse('blog-article', kwargs={'pk':'1' , 'slug':'test-article'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_type_school(self):
        # test the type view when passing in a school
        url = reverse('blog-type', kwargs={'pk':'1' , 'slug':'test-article', 'type':'school'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_type_property(self):
        # test the type view when passing in a property
        url = reverse('blog-type', kwargs={'pk':'1' , 'slug':'test-article', 'type':'property'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

