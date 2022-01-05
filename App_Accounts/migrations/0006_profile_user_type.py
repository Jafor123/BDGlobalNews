# Generated by Django 3.2.7 on 2021-09-21 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Accounts', '0005_auto_20210918_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.CharField(blank=True, choices=[('App_Author', 'App_Author'), ('Editor', 'Editor'), ('Subscriber', 'Subscriber')], default='Subscriber', max_length=30),
        ),
    ]