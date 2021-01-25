# core/routing.py
from django.conf.urls import url

from core import consumers

websocket_urlpatterns = [
    url(r'^ws$', consumers.ChatConsumer),
]
