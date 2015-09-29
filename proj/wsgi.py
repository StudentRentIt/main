"""
WSGI config for the RentVersity project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.environ["SETTINGS_LOCATION"])

# TODO: this should use whitenoise in deployed instances
if os.environ['SETTINGS_LOCATION'] != 'settings.local_adam':
    application = DjangoWhiteNoise(application)
else:
    application = get_wsgi_application()
