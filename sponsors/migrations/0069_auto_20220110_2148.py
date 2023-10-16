# Generated by Django 2.2.24 on 2022-01-10 21:48

import django.db.models.deletion
from django.db import (
    migrations,
    models,
)

import sponsors.models.benefits


class Migration(migrations.Migration):
    dependencies = [
        ('sponsors', '0068_auto_20220110_1841'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProvidedTextAsset',
            fields=[
                (
                    'benefitfeature_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to='sponsors.BenefitFeature',
                    ),
                ),
                (
                    'related_to',
                    models.CharField(
                        choices=[
                            ('sponsor', 'Sponsor'),
                            ('sponsorship', 'Sponsorship'),
                        ],
                        help_text='To which instance (Sponsor or Sponsorship) should this asset relate to.',
                        max_length=30,
                        verbose_name='Related To',
                    ),
                ),
                (
                    'internal_name',
                    models.CharField(
                        db_index=True,
                        help_text='Unique name used internally to control if the sponsor/sponsorship already has the asset',
                        max_length=128,
                        verbose_name='Internal Name',
                    ),
                ),
                (
                    'label',
                    models.CharField(
                        help_text="What's the title used to display the text input to the sponsor?",
                        max_length=256,
                    ),
                ),
                (
                    'help_text',
                    models.CharField(
                        blank=True,
                        default='',
                        help_text='Any helper comment on how the input should be populated',
                        max_length=256,
                    ),
                ),
            ],
            options={
                'verbose_name': 'Provided Text',
                'verbose_name_plural': 'Provided Texts',
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=(
                sponsors.models.benefits.ProvidedAssetMixin,
                'sponsors.benefitfeature',
                models.Model,
            ),
        ),
        migrations.CreateModel(
            name='ProvidedTextAssetConfiguration',
            fields=[
                (
                    'benefitfeatureconfiguration_ptr',
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to='sponsors.BenefitFeatureConfiguration',
                    ),
                ),
                (
                    'related_to',
                    models.CharField(
                        choices=[
                            ('sponsor', 'Sponsor'),
                            ('sponsorship', 'Sponsorship'),
                        ],
                        help_text='To which instance (Sponsor or Sponsorship) should this asset relate to.',
                        max_length=30,
                        verbose_name='Related To',
                    ),
                ),
                (
                    'internal_name',
                    models.CharField(
                        db_index=True,
                        help_text='Unique name used internally to control if the sponsor/sponsorship already has the asset',
                        max_length=128,
                        verbose_name='Internal Name',
                    ),
                ),
                (
                    'label',
                    models.CharField(
                        help_text="What's the title used to display the text input to the sponsor?",
                        max_length=256,
                    ),
                ),
                (
                    'help_text',
                    models.CharField(
                        blank=True,
                        default='',
                        help_text='Any helper comment on how the input should be populated',
                        max_length=256,
                    ),
                ),
            ],
            options={
                'verbose_name': 'Provided Text Configuration',
                'verbose_name_plural': 'Provided Text Configurations',
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=(
                sponsors.models.benefits.AssetConfigurationMixin,
                'sponsors.benefitfeatureconfiguration',
                models.Model,
            ),
        ),
        migrations.AddConstraint(
            model_name='providedtextassetconfiguration',
            constraint=models.UniqueConstraint(
                fields=('internal_name',),
                name='uniq_provided_text_asset_cfg',
            ),
        ),
    ]
