# Generated by Django 5.0.1 on 2024-01-28 00:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0006_buyer_payment_date'),
        ('information', '0017_alter_information_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='information',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='information.information'),
        ),
    ]