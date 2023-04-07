import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
import Chat.routing
# from home.consumer import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChatApp.settings')

application = get_asgi_application()


# ws_patterns = [
#     path('ws/test/',TestConsumer)
# ]

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(
    Chat.routing.websocket_urlpatterns
    )
})
