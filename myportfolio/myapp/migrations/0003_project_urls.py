# Generated by Django 5.1.7 on 2025-03-13 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='urls',
            field=models.URLField(blank=True, null=True),
        ),
    ]
