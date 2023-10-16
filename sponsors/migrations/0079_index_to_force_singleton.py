# Generated by Django 2.2.24 on 2022-07-28 16:20

from django.db import (
    migrations,
)

# This commands creates a unique index on the table but not on top of a column, but on the value true.
# That way, every time we try to insert in this table, the unique constraint will be violated because
# the row trying to be inserted will have the same true value for this index, thus, not unique.
CREATE_SINGLETON_INDEX = """
CREATE UNIQUE INDEX "sponsorship_current_year_singleton_idx" 
ON \"sponsors_sponsorshipcurrentyear\" ((true));
""".strip()

DROP_SINGLETON_INDEX = """
DROP INDEX IF EXISTS "sponsorship_current_year_singleton_idx"; 
""".strip()


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('sponsors', '0078_init_current_year_singleton'),
    ]

    operations = [
        migrations.RunSQL(
            sql=CREATE_SINGLETON_INDEX,
            reverse_sql=DROP_SINGLETON_INDEX,
        ),
    ]
