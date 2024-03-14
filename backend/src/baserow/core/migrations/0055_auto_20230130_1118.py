# Generated by Django 3.2.13 on 2023-01-30 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0054_rename_group_installtemplatejob_workspace"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workspaceinvitation",
            name="permissions",
            field=models.CharField(
                default="MEMBER",
                help_text="The permissions that the user is going to get within the "
                "workspace after accepting the invitation.",
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="workspaceinvitation",
            name="workspace",
            field=models.ForeignKey(
                help_text="The workspace that the user will get access to once the "
                "invitation is accepted.",
                on_delete=django.db.models.deletion.CASCADE,
                to="core.workspace",
            ),
        ),
        migrations.AlterField(
            model_name="workspaceuser",
            name="permissions",
            field=models.CharField(
                default="MEMBER",
                help_text="The permissions that the user has within the workspace.",
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="workspaceuser",
            name="workspace",
            field=models.ForeignKey(
                help_text="The workspace that the user has access to.",
                on_delete=django.db.models.deletion.CASCADE,
                to="core.workspace",
            ),
        ),
    ]
