# Generated by Django 4.2.14 on 2024-07-30 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productmodel",
            name="image",
            field=models.ImageField(
                default="/default/prod-def.png", upload_to="products/img"
            ),
        ),
    ]
