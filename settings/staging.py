from .base import *

# production environment
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['test.rentversity.com']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'studentrentit$dev',                      # Or path to database file if using sqlite3. '/home/studentrentit/dev/main/dev.db'
        'USER': 'studentrentit',                      # Not used with sqlite3.
        'PASSWORD': 'student12',                  # Not used with sqlite3.
        'HOST': 'mysql.server',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.\
        'TEST_NAME': 'studentrentit$test_dev',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static")

#Used in the emails to get the image link
WEB_URL_ROOT = 'https://test.rentversity.com/'