# Generated by Django 3.2.7 on 2021-09-18 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Accounts', '0004_alter_profile_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fb_id',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instra_id',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkd_id',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='tw_id',
            field=models.URLField(blank=True),
        ),
    ]
