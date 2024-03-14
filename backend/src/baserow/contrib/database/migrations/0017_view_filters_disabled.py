# Generated by Django 2.2.11 on 2020-10-25 22:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0016_token_tokenpermission"),
    ]

    operations = [
        migrations.AddField(
            model_name="view",
            name="filters_disabled",
            field=models.BooleanField(
                default=False,
                help_text="Allows users to see results unfiltered "
                "while still keeping the filters for the view"
                "saved.",
            ),
        ),
    ]