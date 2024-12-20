"""
WSGI config for chatbot_project.

It exposes the WSGI callable as a module-level variable named `application`.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbot_project.settings')

# Get the WSGI application callable
application = get_wsgi_application()
