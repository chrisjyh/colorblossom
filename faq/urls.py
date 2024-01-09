from django.urls import path
from . import views

urlpatterns = [
    path("", views.faqTemplate, name="faqPage"),
    path("/community", views.askInformation, name="askInformationPage"),
    path("/askform", views.askform, name="askForm"),
]
