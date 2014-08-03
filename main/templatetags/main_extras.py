from django import template

from property.utils import get_review_person

register = template.Library()

@register.filter(name='get_image_url')
def get_image_url(value):
    """Removes all values of arg from the given string"""
    id = value.replace('https://plus.google.com/', '')
    data = get_review_person(id)
    url = data.get("image").get("url")

    return url