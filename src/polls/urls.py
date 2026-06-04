from django.urls import path

from . import views
from .views import telegram_webhook

urlpatterns = [
    path("telegram/", telegram_webhook),
]
