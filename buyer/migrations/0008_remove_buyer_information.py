# Generated by Django 5.0.1 on 2024-01-28 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0007_buyer_information'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='information',
        ),
    ]
