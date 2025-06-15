from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import BeginningPage

@admin.register(BeginningPage)
class BeginningPageAdmin(MarkdownxModelAdmin):
    list_display = ("title",)
