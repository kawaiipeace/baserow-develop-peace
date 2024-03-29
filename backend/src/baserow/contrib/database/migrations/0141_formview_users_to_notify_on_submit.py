# Generated by Django 3.2.21 on 2023-11-03 13:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("database", "0140_lastmodifiedbyfield"),
    ]

    operations = [
        migrations.AddField(
            model_name="formview",
            name="users_to_notify_on_submit",
            field=models.ManyToManyField(
                help_text="The users that must be notified when the form is submitted.",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
