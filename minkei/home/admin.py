from django.contrib import admin

from .models import SiteNews


@admin.register(SiteNews)
class SiteNewsAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date", "is_published", "updated_at")
    list_filter = ("is_published", "published_date")
    search_fields = ("title", "body")
