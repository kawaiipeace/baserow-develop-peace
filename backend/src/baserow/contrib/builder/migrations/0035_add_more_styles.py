# Generated by Django 3.2.21 on 2023-12-19 13:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("builder", "0034_dropdownelement_dropdownelementoption"),
    ]

    operations = [
        migrations.AddField(
            model_name="buttonelement",
            name="button_color",
            field=models.CharField(
                blank=True,
                default="primary",
                help_text="The color of the button",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="element",
            name="style_border_left_color",
            field=models.CharField(
                blank=True,
                default="border",
                help_text="Left border color",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="element",
            name="style_border_left_size",
            field=models.PositiveIntegerField(
                default=0, help_text="Pixel height of the left border."
            ),
        ),
        migrations.AddField(
            model_name="element",
            name="style_border_right_color",
            field=models.CharField(
                blank=True,
                default="border",
                help_text="Right border color",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="element",
            name="style_border_right_size",
            field=models.PositiveIntegerField(
                default=0, help_text="Pixel height of the right border."
            ),
        ),
        migrations.AddField(
            model_name="element",
            name="style_padding_left",
            field=models.PositiveIntegerField(
                default=20, help_text="Padding size of the left border."
            ),
        ),
        migrations.AddField(
            model_name="element",
            name="style_padding_right",
            field=models.PositiveIntegerField(
                default=20, help_text="Padding size of the right border."
            ),
        ),
        migrations.AddField(
            model_name="formcontainerelement",
            name="button_color",
            field=models.CharField(
                blank=True,
                default="primary",
                help_text="The color of the button",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="linkelement",
            name="button_color",
            field=models.CharField(
                blank=True,
                default="primary",
                help_text="The color of the button",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="tableelement",
            name="button_color",
            field=models.CharField(
                blank=True,
                default="primary",
                help_text="The color of the button",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="columnelement",
            name="column_gap",
            field=models.IntegerField(
                default=20,
                help_text="The amount of space between the columns.",
                validators=[
                    django.core.validators.MinValueValidator(
                        0, message="Value cannot be less than 0."
                    ),
                    django.core.validators.MaxValueValidator(
                        2000, message="Value cannot be greater than 2000."
                    ),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="element",
            name="style_padding_bottom",
            field=models.PositiveIntegerField(
                default=10, help_text="Padding size of the bottom border."
            ),
        ),
        migrations.AlterField(
            model_name="element",
            name="style_padding_top",
            field=models.PositiveIntegerField(
                default=10, help_text="Padding size of the top border."
            ),
        ),
    ]
