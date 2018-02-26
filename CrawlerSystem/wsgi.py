"""
WSGI config for crawlerSystem project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"CrawlerSystem")))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CrawlerSystem.settings")

application = get_wsgi_application()