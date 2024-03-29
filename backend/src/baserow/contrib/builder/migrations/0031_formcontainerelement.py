# Generated by Django 3.2.21 on 2023-12-06 09:52

import django.db.models.deletion
from django.db import migrations, models

import baserow.core.formula.field


class Migration(migrations.Migration):
    dependencies = [
        ("builder", "0030_builderworkflowaction_order"),
    ]

    operations = [
        migrations.CreateModel(
            name="FormContainerElement",
            fields=[
                (
                    "element_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="builder.element",
                    ),
                ),
                (
                    "submit_button_label",
                    baserow.core.formula.field.FormulaField(default=""),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("builder.element",),
        ),
    ]
