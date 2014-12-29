from .base import *

# production environment
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['staging.rentversity.com']

STATIC_ROOT = os.path.join(BASE_DIR, "static")

#Used in the emails to get the image link
WEB_URL_ROOT = 'https://test.rentversity.com/'