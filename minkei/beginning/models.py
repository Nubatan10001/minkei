from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

class BeginningPage(models.Model):
    title = models.CharField(max_length=255, verbose_name="タイトル")
    content = MarkdownxField(verbose_name="本文 (Markdown対応)")
    image = models.ImageField(upload_to='beginning/', blank=True, null=True, verbose_name="画像 (任意)")

    def formatted_markdown(self):
        return markdownify(self.content)

    def __str__(self):
        return self.title
