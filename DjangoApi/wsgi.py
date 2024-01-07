"""
WSGI config for DjangoApi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""
import sys
import os

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/Sk0909/DjangoApi')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoApi.settings')

application = get_wsgi_application()