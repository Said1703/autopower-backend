# Generated by Django 5.0.1 on 2024-01-24 01:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0016_information_subscription'),
        ('subscription', '0009_remove_subscription_precio_subscription_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='subscription',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subscription.subscription'),
        ),
    ]
