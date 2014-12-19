'''
Test settings and globals which
allow us to run our test suite
locally.
'''

from .base import *

SOUTH_TESTS_MIGRATE = False

########## IN-MEMORY TEST DATABASE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
}