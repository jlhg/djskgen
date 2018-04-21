from django.conf.urls import include
from django.urls import path

from app import urls as app_urls

urlpatterns = [
    path('', include(app_urls)),
]
