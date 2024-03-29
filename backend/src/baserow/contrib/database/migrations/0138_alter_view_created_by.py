# Generated by Django 3.2.21 on 2023-10-11 14:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("database", "0137_alter_table_last_modified_by_column_added"),
    ]

    operations = [
        migrations.AlterField(
            model_name="view",
            name="created_by",
            field=models.ForeignKey(
                db_column="created_by_id",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
