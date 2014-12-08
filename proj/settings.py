"""
Django settings for dev project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

if BASE_DIR == "'/home/studentrentit/rentversity'":
    # production environment
    SECRET_KEY = '5@1f7zdj%2v42o75CsZ@)4tcjkadued8y(_^wn@kha8dpn5vnf'
    DEBUG = False
    TEMPLATE_DEBUG = False
    ALLOWED_HOSTS = ['rentversity.studentrentit.com']


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
else:
    # local environment
    SECRET_KEY = '5@1f7zdj%2v42o75bs2@)4tcjkcoueb8y(_^wn@khr8dpn5vmf'
    DEBUG = True
    TEMPLATE_DEBUG = True
    ALLOWED_HOSTS = []

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': '/Users/awwester/Sites/sri/site/db/local.sql',                      # Or path to database file if using sqlite3. '/home/studentrentit/dev/main/dev.db'
            'TEST_NAME': 'studentrentit$test_dev',
        }
    }

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
    )



#500 error emails
ADMINS = (
    ('Adam', 'awwester@gmail.com'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'allauth', #used for social logins as well as normal login/registration
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'localflavor', #used for US model fields
    'south',
    'braces',
    'crispy_forms',
    'flowcore',
    'flowreport',
    'main',
    'property',
    'school',
    'blog',
    'campusamb',
    'search',
    'scrape',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'proj.urls'
WSGI_APPLICATION = 'proj.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

import sys
if 'test' in sys.argv or 'test_coverage' in sys.argv: #Covers regular testing and django-coverage
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'
    DATABASES['default']['NAME'] = '/home/studentrentit/dev/test.db'

#disable south migrations while testing
SOUTH_TESTS_MIGRATE = False

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True

TIME_INPUT_FORMATS = (
    '%H:%M:%S',     # '14:30:59'
    '%H:%M:%S.%f',  # '14:30:59.000200'
    '%H:%M',        # '14:30'
    '%I:%M%p',      # support for am/pm
    '%I:%M %p',
    '%I%p',         # am/pm without minutes
    '%I %p',
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_URL = '/static/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media' )
MEDIA_URL = '/media/'

#Used in the emails to get the image link
WEB_URL_ROOT = 'http://127.0.0.1:8000/'

#used for django-allauth app
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
    'main.context_processors.all_schools',
    'main.context_processors.all_cities',
    'main.context_processors.get_user_items',
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'support@studentrentit.com'
EMAIL_HOST_PASSWORD = 'sri123qwe'
EMAIL_USE_TLS = True
SERVER_EMAIL = 'support@studentrentit.com'

#turn off emails
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#settings for all-auth
SITE_ID=1
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True

LOGIN_REDIRECT_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email', 'publish_stream'],
        'METHOD': 'js_sdk'  # instead of 'oauth2'
    }
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
         'require_debug_false': {
             '()': 'django.utils.log.RequireDebugFalse',
         }
     },
     'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

STRIPE_SECRET_KEY = 'sk_test_BU1tsOK2ERirE6WsvDHfYCwt'
STRIPE_PUBLIC_KEY = 'pk_test_Myf83zAyJEPV6SinLgrgYc29'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

GOOGLE_API_KEY = 'AIzaSyCQ9s21SXE_4jk3r2T030gWcXFyTAii6HQ'
WALKSCORE_API_KEY = 'df07b2fb3c9c862c3d960e4802c352be'