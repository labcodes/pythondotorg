# Generated by Django 2.2.24 on 2021-12-23 13:09

from django.db import (
    migrations,
)
from django.utils.text import (
    slugify,
)


def populate_packages_slugs(apps, schema_editor):
    SponsorshipPackage = apps.get_model("sponsors", "SponsorshipPackage")
    qs = SponsorshipPackage.objects.filter(slug="")
    for pkg in qs:
        pkg.slug = slugify(pkg.name)
        pkg.save()


class Migration(migrations.Migration):
    dependencies = [
        ('sponsors', '0064_sponsorshippackage_slug'),
    ]

    operations = [
        migrations.RunPython(populate_packages_slugs, migrations.RunPython.noop)
    ]
