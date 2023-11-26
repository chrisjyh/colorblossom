
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('faq/', include("faq.urls")),
    path('selftest/', include("selftest.urls")),
    path("", TemplateView.as_view(template_name="main.html"), name="main")
]


if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include("debug_toolbar.urls")),
    ]
    
