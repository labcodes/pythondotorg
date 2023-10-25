# Generated by Django 2.2.24 on 2022-03-03 20:23

import django.db.models.deletion
import django.db.models.manager
from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):
    dependencies = [
        ("sponsors", "0074_auto_20220211_1659"),
    ]

    operations = [
        migrations.AddField(
            model_name="sponsorship",
            name="overlapped_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="sponsors.Sponsorship",
            ),
        ),
    ]
