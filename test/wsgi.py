"""
WSGI config for test project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings_module = 'test.deployement_settings' if 'RENDER_EXTRENAL_HOSTNAME' in os.environ else 'test.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test.settings')

application = get_wsgi_application()
