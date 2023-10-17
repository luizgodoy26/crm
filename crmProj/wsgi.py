"""
WSGI config for crmProj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

# https://www.youtube.com/watch?v=QjEVmQ4rcWA

settings_module = 'crmProj.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'crmProj.settings'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = Cling(get_wsgi_application())
