# Generated by Django 4.2.14 on 2024-12-28 16:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0006_alter_ordermodel_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="couponmodel",
            name="discount_percent",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="couponmodel",
            name="max_limit_usage",
            field=models.IntegerField(),
        ),
    ]
