from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import MicroEconArticle

@admin.register(MicroEconArticle)
class MicroEconArticleAdmin(MarkdownxModelAdmin):
    list_display = ('title', 'published_date', 'updated_date')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content')
