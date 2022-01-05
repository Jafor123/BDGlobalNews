# Generated by Django 3.2.7 on 2021-09-22 08:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App_News', '0024_alter_news_publish_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='dislike',
        ),
        migrations.AddField(
            model_name='news',
            name='spam',
            field=models.ManyToManyField(blank=True, related_name='spam', to=settings.AUTH_USER_MODEL),
        ),
    ]
