# Generated by Django 3.2.7 on 2021-09-14 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_News', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App_News.category'),
        ),
        migrations.AlterField(
            model_name='news',
            name='sub_category_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App_News.subcategory'),
        ),
    ]