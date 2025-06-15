from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import RoadmapPage

@admin.register(RoadmapPage)
class RoadmapPageAdmin(MarkdownxModelAdmin):
    list_display = ("title",)
