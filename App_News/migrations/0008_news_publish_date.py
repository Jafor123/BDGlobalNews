# Generated by Django 3.2.7 on 2021-09-15 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_News', '0007_auto_20210915_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='publish_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
