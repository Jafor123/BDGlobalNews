# Generated by Django 3.2.7 on 2021-09-17 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_News', '0019_alter_comment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='language',
        ),
    ]
