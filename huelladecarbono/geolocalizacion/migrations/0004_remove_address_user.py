# Generated by Django 2.1.12 on 2020-11-24 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geolocalizacion', '0003_address_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='user',
        ),
    ]
