# Generated by Django 3.2.7 on 2021-09-14 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, choices=[('UK', 'United Kingdom'), ('US', 'United States'), ('BD', 'Bangladesh'), ('Others', 'Others')], max_length=50),
        ),
    ]
