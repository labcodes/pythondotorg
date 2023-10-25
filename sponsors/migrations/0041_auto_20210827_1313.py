# Generated by Django 2.0.13 on 2021-08-27 13:13

from django.db import (
    migrations,
)


def populate_logo_dimensions(apps, schema_editor):
    SponsorshipPackage = apps.get_model("sponsors.SponsorshipPackage")
    logo_dimensions = {
        "Visionary": 350,
        "Sustainability": 300,
        "Maintaining": 300,
        "Contributing": 275,
        "Supporting": 250,
        "Partner": 225,
        "Participating": 225,
        "Associate": 175,
    }

    for name, dimension in logo_dimensions.items():
        SponsorshipPackage.objects.filter(name=name).update(logo_dimension=dimension)


def reset_logo_dimensions(apps, schema_editor):
    SponsorshipPackage = apps.get_model("sponsors.SponsorshipPackage")
    SponsorshipPackage.objects.all().update(logo_dimension=175)


class Migration(migrations.Migration):
    dependencies = [
        ("sponsors", "0040_auto_20210827_1313"),
    ]

    operations = [migrations.RunPython(populate_logo_dimensions, reset_logo_dimensions)]
