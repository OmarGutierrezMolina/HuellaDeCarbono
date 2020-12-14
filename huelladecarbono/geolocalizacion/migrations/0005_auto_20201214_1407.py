# Generated by Django 2.1.12 on 2020-12-14 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geolocalizacion', '0004_auto_20201214_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='comuna',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='geolocalizacion.Comuna'),
        ),
        migrations.AddField(
            model_name='address',
            name='provincia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='geolocalizacion.Provincia'),
        ),
        migrations.AddField(
            model_name='address',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='geolocalizacion.Region'),
        ),
    ]
