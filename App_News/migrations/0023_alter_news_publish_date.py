# Generated by Django 3.2.7 on 2021-09-19 08:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_News', '0022_alter_news_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='publish_date',
            field=models.DateField(blank=True, default=datetime.date(2021, 9, 19), null=True),
        ),
    ]
