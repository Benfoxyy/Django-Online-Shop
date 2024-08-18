# Generated by Django 4.2.14 on 2024-07-31 10:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_productmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='discount_percent',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]