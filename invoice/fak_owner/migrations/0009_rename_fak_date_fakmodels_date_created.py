# Generated by Django 5.0 on 2024-01-10 20:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("fak_owner", "0008_alter_fakmodels_fak_date"),
    ]

    operations = [
        migrations.RenameField(
            model_name="fakmodels",
            old_name="fak_date",
            new_name="date_created",
        ),
    ]