# Generated by Django 5.0.4 on 2024-06-01 08:46

from django.db import migrations, models

import django_paddle_billing.encoders


class Migration(migrations.Migration):

    dependencies = [
        ("django_paddle_billing", "0002_alter_subscription_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="Discount",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("occurred_at", models.DateTimeField(blank=True, null=True)),
                ("id", models.CharField(max_length=50, primary_key=True, serialize=False)),
                (
                    "data",
                    models.JSONField(blank=True, encoder=django_paddle_billing.encoders.PrettyJSONEncoder, null=True),
                ),
                (
                    "custom_data",
                    models.JSONField(blank=True, encoder=django_paddle_billing.encoders.PrettyJSONEncoder, null=True),
                ),
            ],
        ),
    ]
