# Generated by Django 2.2.24 on 2021-08-19 13:16

from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):
    dependencies = [
        ("sponsors", "0044_auto_20210827_1344"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sponsorbenefit",
            name="added_by_user",
            field=models.BooleanField(
                blank=True,
                default=False,
                verbose_name="Added by user?",
            ),
        ),
    ]
