# Generated by Django 5.1.7 on 2025-03-20 09:15

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='file',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='file'),
        ),
    ]
