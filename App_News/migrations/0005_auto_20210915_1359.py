# Generated by Django 3.2.7 on 2021-09-15 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_News', '0004_alter_news_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='category_name',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='sub_category_name',
            new_name='subcategory',
        ),
    ]