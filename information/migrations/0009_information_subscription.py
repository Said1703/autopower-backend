# Generated by Django 5.0 on 2024-01-21 04:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0008_autos_remove_information_direccion_and_more'),
        ('subscription', '0004_alter_subscription_planes'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='subscription',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='subscription.subscription'),
        ),
    ]
