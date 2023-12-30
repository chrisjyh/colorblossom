from urllib import request

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('faq/', include("faq.urls")),
    path('selftest/', TemplateView.as_view(template_name="selftest/selftest.html"), name="selftest"),
    path("", views.index, name="main")
]


if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include("debug_toolbar.urls")),
    ]
    
