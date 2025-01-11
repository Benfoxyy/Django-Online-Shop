# Generated by Django 4.2.14 on 2024-12-29 17:22

import accounts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticketmodel",
            name="phone_number",
            field=models.CharField(
                blank=True,
                max_length=12,
                null=True,
                validators=[
                    accounts.validators.validate_iranian_cellphone_number
                ],
            ),
        ),
    ]
