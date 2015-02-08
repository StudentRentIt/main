from .staging import *

ALLOWED_HOSTS = ['www.rentversity.com']
WEB_URL_ROOT = 'https://www.rentversity.com/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'studentrentit$rvprod',                      # Or path to database file if using sqlite3. '/home/studentrentit/dev/main/dev.db'
        'USER': 'studentrentit',                      # Not used with sqlite3.
        'PASSWORD': 'student12',                  # Not used with sqlite3.
        'HOST': 'mysql.server',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.\
        'TEST_NAME': 'studentrentit$test_dev',
    }
}