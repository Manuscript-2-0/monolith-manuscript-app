# Generated by Django 4.1.5 on 2023-01-28 08:42

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_event_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to=app.models.upload_to
            ),
        ),
    ]