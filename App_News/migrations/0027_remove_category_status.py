# Generated by Django 3.2.7 on 2021-09-22 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_News', '0026_category_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='status',
        ),
    ]