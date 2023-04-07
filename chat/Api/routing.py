from django.urls import re_path
from django.core.asgi import get_asgi_application
from channels.routing import URLRouter
from .consumers import LongPollConsumer

application = get_asgi_application()

websocket_urlpatterns = []

urlpatterns = [
    re_path(r"^longpoll/$", LongPollConsumer.as_asgi()),
    re_path(r"^notifications/(?P<stream>\w+)/$", LongPollConsumer.as_asgi()),
]

application = URLRouter(websocket_urlpatterns + urlpatterns)
