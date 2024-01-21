# Generated by Django 5.0 on 2024-01-21 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0003_subscription_planes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='planes',
            field=models.CharField(choices=[('basic', 10), ('gold', 20), ('platinum', 30)], max_length=20, null=True),
        ),
    ]
