# Generated by Django 2.2.24 on 2023-02-14 21:13

from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):
    dependencies = [
        ("sponsors", "0092_auto_20220816_1517"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sponsorshipbenefit",
            name="package_only",
            field=models.BooleanField(
                default=False,
                help_text="If a benefit is only available via a sponsorship package and not as an add-on, select this option.",
                verbose_name="Sponsor Package Only Benefit",
            ),
        ),
    ]
