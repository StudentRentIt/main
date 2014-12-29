from .base import *

# production environment
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['test.rentversity.com']

STATIC_ROOT = os.path.join(BASE_DIR, "static")

#Used in the emails to get the image link
WEB_URL_ROOT = 'https://test.rentversity.com/'