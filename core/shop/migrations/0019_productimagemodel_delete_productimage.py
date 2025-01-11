# Generated by Django 4.2.14 on 2025-01-03 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0018_alter_productimage_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductImageModel",
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
                (
                    "image",
                    models.ImageField(
                        default="default/proddef.png",
                        upload_to="products/img",
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now=True)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_image_related",
                        to="shop.productmodel",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="ProductImage",
        ),
    ]