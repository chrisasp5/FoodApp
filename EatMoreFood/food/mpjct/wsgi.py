"""
WSGI config for mpjct project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mpjct.settings")

application = get_wsgi_application()

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'cq4z!qeu*a65et^c75c&w$@an-eg5=hbgy59yzg17c17h__2$-'
