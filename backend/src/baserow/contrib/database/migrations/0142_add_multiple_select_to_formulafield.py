# Generated by Django 3.2.21 on 2023-10-31 10:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0141_formview_users_to_notify_on_submit"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formulafield",
            name="array_formula_type",
            field=models.TextField(
                choices=[
                    ("invalid", "invalid"),
                    ("text", "text"),
                    ("char", "char"),
                    ("link", "link"),
                    ("date_interval", "date_interval"),
                    ("date", "date"),
                    ("boolean", "boolean"),
                    ("number", "number"),
                    ("single_select", "single_select"),
                    ("multiple_select", "multiple_select"),
                    ("single_file", "single_file"),
                ],
                default=None,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="formulafield",
            name="formula_type",
            field=models.TextField(
                choices=[
                    ("invalid", "invalid"),
                    ("text", "text"),
                    ("char", "char"),
                    ("link", "link"),
                    ("date_interval", "date_interval"),
                    ("date", "date"),
                    ("boolean", "boolean"),
                    ("number", "number"),
                    ("array", "array"),
                    ("single_select", "single_select"),
                    ("multiple_select", "multiple_select"),
                    ("single_file", "single_file"),
                ],
                default="invalid",
            ),
        ),
    ]
