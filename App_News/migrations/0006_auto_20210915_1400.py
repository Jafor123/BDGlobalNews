# Generated by Django 3.2.7 on 2021-09-15 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_News', '0005_auto_20210915_1359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='category_name',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='subcategory',
            old_name='sub_category_name',
            new_name='name',
        ),
    ]
