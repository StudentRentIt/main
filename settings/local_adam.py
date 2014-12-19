from .dev import *

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(BASE_DIR, 'db/local.sql'),
    }
}


STATIC_ROOT = ""
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

#Used in the emails to get the image link
WEB_URL_ROOT = 'http://127.0.0.1:8000/'
