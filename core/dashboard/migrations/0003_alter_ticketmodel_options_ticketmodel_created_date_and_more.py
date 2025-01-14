# Generated by Django 4.2.14 on 2024-12-29 17:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0002_alter_ticketmodel_phone_number"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ticketmodel",
            options={"ordering": ["-created_date"]},
        ),
        migrations.AddField(
            model_name="ticketmodel",
            name="created_date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="ticketmodel",
            name="updated_date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
