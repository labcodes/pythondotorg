# Generated by Django 2.2.24 on 2021-11-11 15:29

from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):
    dependencies = [("sponsors", "0061_auto_20211108_1419")]

    operations = [
        migrations.AlterField(
            model_name="logoplacement",
            name="describe_as_sponsor",
            field=models.BooleanField(
                default=False,
                help_text='Override description with "SPONSOR_NAME is a SPONSOR_LEVEL sponsor of the Python Software Foundation".',
            ),
        ),
        migrations.AlterField(
            model_name="logoplacement",
            name="link_to_sponsors_page",
            field=models.BooleanField(
                default=False,
                help_text="Override URL in placement to the PSF Sponsors Page, rather than the sponsor landing page url.",
            ),
        ),
        migrations.AlterField(
            model_name="logoplacementconfiguration",
            name="describe_as_sponsor",
            field=models.BooleanField(
                default=False,
                help_text='Override description with "SPONSOR_NAME is a SPONSOR_LEVEL sponsor of the Python Software Foundation".',
            ),
        ),
        migrations.AlterField(
            model_name="logoplacementconfiguration",
            name="link_to_sponsors_page",
            field=models.BooleanField(
                default=False,
                help_text="Override URL in placement to the PSF Sponsors Page, rather than the sponsor landing page url.",
            ),
        ),
    ]
