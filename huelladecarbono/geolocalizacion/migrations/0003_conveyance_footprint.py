# Generated by Django 2.1.12 on 2020-12-09 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geolocalizacion', '0002_auto_20201209_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='conveyance',
            name='footprint',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]