# Generated by Django 3.2.7 on 2021-09-16 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_News', '0018_comment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]