# Generated by Django 2.1.12 on 2020-12-09 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geolocalizacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='conveyance',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='geolocalizacion.Conveyance', verbose_name='Medio de transporte'),
        ),
        migrations.AlterField(
            model_name='address',
            name='destination',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='geolocalizacion.Destination'),
        ),
    ]
