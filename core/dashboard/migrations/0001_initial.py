# Generated by Django 4.2.14 on 2024-12-29 17:01

import accounts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TicketModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                (
                    "phone_number",
                    models.CharField(
                        max_length=12,
                        validators=[
                            accounts.validators.validate_iranian_cellphone_number
                        ],
                    ),
                ),
                ("description", models.TextField()),
            ],
        ),
    ]
