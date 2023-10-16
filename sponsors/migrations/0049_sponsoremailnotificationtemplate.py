# Generated by Django 2.2.24 on 2021-09-15 14:41

from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):
    dependencies = [
        ('sponsors', '0048_auto_20210915_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='SponsorEmailNotificationTemplate',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('internal_name', models.CharField(max_length=128)),
                ('subject', models.CharField(max_length=128)),
                ('content', models.TextField()),
                (
                    'created_at',
                    models.DateTimeField(auto_now_add=True),
                ),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Sponsor Email Notification Template',
                'verbose_name_plural': 'Sponsor Email Notification Templates',
            },
        ),
    ]
