# Generated by Django 2.0.13 on 2021-08-27 12:23

import django.db.models.deletion
from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):
    dependencies = [
        ("sponsors", "0036_auto_20210826_1930"),
    ]

    operations = [
        migrations.AddField(
            model_name="sponsorship",
            name="package",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="sponsors.SponsorshipPackage",
            ),
        ),
    ]
