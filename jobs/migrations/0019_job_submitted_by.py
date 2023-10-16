# Generated by Django 2.0.13 on 2019-09-06 20:29

import django.db.models.deletion
from django.conf import (
    settings,
)
from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0018_auto_20180705_0352'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='submitted_by',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
