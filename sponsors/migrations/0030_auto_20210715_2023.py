# Generated by Django 2.0.13 on 2021-07-15 20:23

import django.db.models.deletion
from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):
    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("sponsors", "0029_auto_20210715_2015"),
    ]

    operations = [
        migrations.CreateModel(
            name="BenefitFeature",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "Benefit Feature",
                "verbose_name_plural": "Benefit Features",
            },
        ),
        migrations.AlterModelOptions(
            name="logoplacementconfiguration",
            options={
                "base_manager_name": "objects",
                "verbose_name": "Logo Placement Configuration",
                "verbose_name_plural": "Logo Placement Configurations",
            },
        ),
        migrations.CreateModel(
            name="LogoPlacement",
            fields=[
                (
                    "benefitfeature_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="sponsors.BenefitFeature",
                    ),
                ),
                (
                    "publisher",
                    models.CharField(
                        choices=[
                            ("psf", "Foundation"),
                            ("pycon", "Pycon"),
                            ("pypi", "Pypi"),
                            ("core", "Core Dev"),
                        ],
                        help_text="On which site should the logo be displayed?",
                        max_length=30,
                        verbose_name="Publisher",
                    ),
                ),
                (
                    "logo_place",
                    models.CharField(
                        choices=[
                            ("sidebar", "Sidebar"),
                            ("sponsors", "Sponsors Page"),
                            ("jobs", "Jobs"),
                            ("blogpost", "Blog"),
                            ("footer", "Footer"),
                            ("docs", "Docs"),
                            ("download", "Download Page"),
                            ("devguide", "Dev Guide"),
                        ],
                        help_text="Where the logo should be placed?",
                        max_length=30,
                        verbose_name="Logo Placement",
                    ),
                ),
            ],
            options={
                "verbose_name": "Logo Placement",
                "verbose_name_plural": "Logo Placement",
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("sponsors.benefitfeature", models.Model),
        ),
        migrations.AddField(
            model_name="benefitfeature",
            name="polymorphic_ctype",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="polymorphic_sponsors.benefitfeature_set+",
                to="contenttypes.ContentType",
            ),
        ),
        migrations.AddField(
            model_name="benefitfeature",
            name="sponsor_benefit",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="sponsors.SponsorBenefit",
            ),
        ),
    ]
