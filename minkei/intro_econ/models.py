from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

class EconArticle(models.Model):
    title = models.CharField(max_length=200, verbose_name="記事タイトル")
    slug = models.SlugField(unique=True, blank=True, null=True)
    content = MarkdownxField(verbose_name="記事内容 (Markdown)")
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']

    def formatted_markdown(self):
        return markdownify(self.content)

    def __str__(self):
        return self.title
