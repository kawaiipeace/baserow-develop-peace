# Generated by Django 4.0.10 on 2024-01-19 05:04

from django.db import migrations


def forward(apps, schema_editor):
    """
    Deletes all snapshot entries that didn't result in an actual snapshot
    being created.
    """

    Snapshot = apps.get_model("core", "Snapshot")
    dangling_snapshots = Snapshot.objects.filter(
        createsnapshotjob__state="failed",
        snapshot_to_application__isnull=True,
        mark_for_deletion=False,
    )
    dangling_snapshots.delete()


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0078_usersource"),
    ]

    operations = [
        migrations.RunPython(forward, migrations.RunPython.noop),
    ]
