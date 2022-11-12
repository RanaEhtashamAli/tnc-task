from django.urls import re_path
from .consumer import TNCConsumer

ws_urlpatterns = [
    re_path('ws/tnc/$', TNCConsumer.as_asgi())
]
