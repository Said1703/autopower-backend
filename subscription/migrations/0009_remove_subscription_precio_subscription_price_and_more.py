# Generated by Django 5.0.1 on 2024-01-24 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0008_remove_subscription_basic_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='precio',
        ),
        migrations.AddField(
            model_name='subscription',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
