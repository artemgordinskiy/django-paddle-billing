# Generated by Django 5.0.4 on 2024-06-01 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_paddle_billing', '0002_alter_subscription_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='account',
        ),
    ]
