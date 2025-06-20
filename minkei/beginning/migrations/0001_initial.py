# Generated by Django 5.1.7 on 2025-03-11 13:06

import markdownx.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeginningPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('content', markdownx.models.MarkdownxField(verbose_name='本文 (Markdown対応)')),
                ('image', models.ImageField(blank=True, null=True, upload_to='beginning/', verbose_name='画像 (任意)')),
            ],
        ),
    ]
