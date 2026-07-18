from django.db import models
from django.utils import timezone


class SiteNews(models.Model):
    title = models.CharField("タイトル", max_length=120)
    body = models.TextField("本文", blank=True)
    published_date = models.DateField("公開日", default=timezone.localdate)
    is_published = models.BooleanField("公開する", default=True)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    class Meta:
        verbose_name = "サイト更新履歴"
        verbose_name_plural = "サイト更新履歴"
        ordering = ["-published_date", "-id"]

    def __str__(self):
        return self.title
