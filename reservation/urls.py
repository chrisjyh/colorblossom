from urllib import request

from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="reservationMain")
]

