"""
WSGI config for the RentVersity project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", os.environ["SETTINGS_LOCATION"])
application = get_wsgi_application()

# TODO: this should use whitenoise in deployed instances
if os.environ['SETTINGS_LOCATION'] != 'settings.local_adam':
    from whitenoise.django import DjangoWhiteNoise
    application = DjangoWhiteNoise(application)
