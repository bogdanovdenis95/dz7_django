# Generated by Django 5.0.6 on 2024-07-10 09:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0015_alter_article_preview"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={"verbose_name": "Статья", "verbose_name_plural": "Статьи"},
        ),
    ]
