# intro_macroecon/admin.py
from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import MacroEconArticle

@admin.register(MacroEconArticle)
class MacroEconArticleAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'published_date', 'updated_date')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
