# Generated by Django 2.2.24 on 2023-02-14 21:13

from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):
    dependencies = [
        ('pages', '0002_auto_20150416_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content_markup_type',
            field=models.CharField(
                choices=[
                    ('', '--'),
                    ('html', 'HTML'),
                    ('plain', 'Plain'),
                    ('markdown', 'Markdown'),
                    ('restructuredtext', 'Restructured Text'),
                    ('markdown_unsafe', 'Markdown (unsafe)'),
                ],
                default='restructuredtext',
                max_length=30,
            ),
        ),
    ]
