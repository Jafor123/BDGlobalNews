# Generated by Django 3.2.7 on 2021-09-17 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_News', '0021_userverify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]
