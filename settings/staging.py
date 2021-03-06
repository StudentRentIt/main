import dj_database_url

from .base import *


# production environment
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['rentversity.herokuapp.com']
WEB_URL_ROOT = 'https://rentversity.herokuapp.com/'

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

DATABASES = {}
DATABASES['default'] =  dj_database_url.config()
