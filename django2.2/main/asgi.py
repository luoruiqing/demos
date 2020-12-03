"""
ASGI config for main project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter
import apps.chat.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": AsgiHandler(),
    # Just HTTP for now. (We can add other protocols later.)
    "websocket": AuthMiddlewareStack(
        URLRouter(
            apps.chat.routing.websocket_urlpatterns
        )
    ),
})
