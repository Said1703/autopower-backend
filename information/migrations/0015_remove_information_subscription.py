# Generated by Django 5.0.1 on 2024-01-24 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0014_information_subscription'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='subscription',
        ),
    ]