# Generated by Django 3.2.7 on 2021-09-23 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Accounts', '0008_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]