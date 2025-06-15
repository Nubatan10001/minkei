from django.db import models


class Prof(models.Model):
    name = models.CharField(max_length=100)  # 運営者名
    biography = models.TextField()  # 経歴
    specialty = models.CharField(max_length=200)  # 専門分野
    profile_image = models.ImageField(upload_to='prof_images/', blank=True, null=True)  # プロフィール画像
    message = models.CharField(max_length=300, blank=True, null=True)  # 300字以内の一言メッセージ

    def __str__(self):
        return self.name  # 管理画面で表示する名前
