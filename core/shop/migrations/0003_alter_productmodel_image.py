# Generated by Django 4.2.14 on 2024-07-30 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_productmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='image',
            field=models.ImageField(default='default/proddef.png', upload_to='products/img'),
        ),
    ]
