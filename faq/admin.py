from django.contrib import admin

from faq.models import Faq


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'useyn']
    list_filter = ['useyn']
