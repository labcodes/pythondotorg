from django.db import (
    migrations,
    models,
)


class Migration(migrations.Migration):
    dependencies = [
        ('successstories', '0006_auto_20170726_0824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='weight',
        ),
    ]
