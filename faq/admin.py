from django.contrib import admin

from faq.models import Faq


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    pass