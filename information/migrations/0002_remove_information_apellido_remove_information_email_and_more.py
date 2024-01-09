# Generated by Django 5.0 on 2024-01-06 23:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='information',
            name='email',
        ),
        migrations.RemoveField(
            model_name='information',
            name='nombre',
        ),
        migrations.AddField(
            model_name='information',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='information',
            name='direccion',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='information',
            name='numero_doc',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='pais',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='information',
            name='placa_vehiculo',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='telefono',
            field=models.FloatField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='tipo_documento',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='tipo_vehiculo',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
