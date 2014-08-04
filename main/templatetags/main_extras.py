from django import template

from property.utils import get_review_person

register = template.Library()

@register.filter(name='get_image_url')
def get_image_url(value):
    '''
    get the image of the google plus user
    '''
    if value:
        id = value.replace('https://plus.google.com/', '')
        data = get_review_person(id)
        url = data.get("image").get("url")
    else:
        # default url if there is no google plus user on the review
        url = "https://lh3.googleusercontent.com/-XdUIqdMkCWA/AAAAAAAAAAI/AAAAAAAAAAA/4252rscbv5M/photo.jpg?sz=50"

    return url