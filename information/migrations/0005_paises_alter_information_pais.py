# Generated by Django 5.0 on 2024-01-10 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0004_alter_information_telefono'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peru', models.CharField(max_length=20)),
                ('venezuela', models.CharField(max_length=20)),
                ('mexico', models.CharField(max_length=20)),
                ('ecuador', models.CharField(max_length=20)),
                ('argentina', models.CharField(max_length=20)),
                ('uruguay', models.CharField(max_length=20)),
                ('chile', models.CharField(max_length=20)),
                ('bolivia', models.CharField(max_length=20)),
                ('paraguay', models.CharField(max_length=20)),
                ('brasil', models.CharField(max_length=20)),
                ('colombia', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'paises',
            },
        ),
        migrations.AlterField(
            model_name='information',
            name='pais',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
