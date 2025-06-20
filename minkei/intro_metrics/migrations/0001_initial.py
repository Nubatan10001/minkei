# Generated by Django 5.1.7 on 2025-03-29 12:46

import markdownx.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetricsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='記事タイトル')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('content', markdownx.models.MarkdownxField(verbose_name='記事内容 (Markdown)')),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-published_date'],
            },
        ),
    ]
