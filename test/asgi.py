"""
ASGI config for test project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test.settings')
settings_module = 'test.deployement_settings' if 'RENDER_EXTRENAL_HOSTNAME' in os.environ else 'test.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_asgi_application()
