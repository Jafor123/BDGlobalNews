# Generated by Django 3.2.7 on 2021-09-22 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_News', '0028_categoryapply'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryapply',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]