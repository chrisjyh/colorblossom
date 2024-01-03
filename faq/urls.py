from django.urls import path
from . import views

urlpatterns = [
    path("", views.faqTemplate, name="faqPage"),
    path("", views.askInformation, name="askInformationPage"),
]
