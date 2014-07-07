from django.utils import unittest
from django.contrib.auth.models import User

from main.models import City
from property.models import Property
from school.models import School
from blog.models import Tag, Article


class BlogTestCase(unittest.TestCase):

    def setUp(self):
        # set up required model instances
        city = City.objects.create(name="Blog Test Town", state="TX")
        user = User.objects.create_user('blogtester', 'blogtester@somewhere.com', 'testpassword')
        school = School.objects.create(city=city, name="Blog Test University",
                        long=-97.1234123, lat=45.7801234)
        property = Property.objects.create(school=school, user=user, title="test property",
                        addr="13 Test St.", city="Test Town", state="TX")

        # set up the school models
        tag1 = Tag.objects.create(tag_name="Tag 1")
        tag2 = Tag.objects.create(tag_name="Tag 2")
        article = Article.objects.create(user=user, school=school, property=property,
                    title="Test Article", body="This is the body of the article.")
        article.tags.add(tag1, tag2)

    def test_models(self):
        tag = Tag.objects.get(id=1)
        article = Article.objects.get(id=1)

