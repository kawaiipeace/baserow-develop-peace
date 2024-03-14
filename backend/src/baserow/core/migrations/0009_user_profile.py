# Generated by Django 2.2.11 on 2021-07-06 12:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def forward(apps, schema_editor):
    """
    Add missing Profile to existing users.
    """
    User = apps.get_model("auth", "User")
    UserProfile = apps.get_model("core", "UserProfile")
    for user in User.objects.all():
        UserProfile.objects.create(user=user)


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0008_trash"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "language",
                    models.TextField(
                        default="en",
                        choices=[("en", "English"), ("fr", "French")],
                        help_text="An ISO 639 language code (with optional variant) "
                        "selected by the user. Ex: en-GB.",
                        max_length=10,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.RunPython(forward, migrations.RunPython.noop),
    ]