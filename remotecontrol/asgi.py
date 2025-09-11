# """
# ASGI config for remotecontrol project.

# It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
# """

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'remotecontrol.settings')

# application = get_asgi_application()

# remotecontrol/asgi.py
import os
from django.core.asgi import get_asgi_application
from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from controller.consumers import DeviceStatusConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'remotecontrol.settings')

# This is the crucial part. We are now defining the complete router here.
application = ProtocolTypeRouter({
    # Django's default handler for standard HTTP requests.
    # We pass this to Daphne so it can serve regular web pages.
    "http": get_asgi_application(),

    # Our custom handler for WebSocket connections.
    "websocket": AuthMiddlewareStack(
        URLRouter([
            # The path to our consumer that handles the real-time connection.
            re_path(r'ws/device/(?P<device_id>[\w-]+)/$', DeviceStatusConsumer.as_asgi()),
        ])
    ),
})
