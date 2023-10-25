# Generated by Django 2.2.24 on 2022-08-12 13:14

from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):
    dependencies = [
        ("sponsors", "0089_auto_20220812_1312"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sponsorbenefit",
            name="standalone",
            field=models.BooleanField(
                blank=True,
                default=False,
                verbose_name="Added as standalone benefit?",
            ),
        ),
        migrations.AlterField(
            model_name="sponsorshipbenefit",
            name="standalone",
            field=models.BooleanField(
                default=False,
                help_text="Standalone benefits can be selected without the need of a package.",
                verbose_name="Standalone",
            ),
        ),
    ]
