# Generated by Django 5.0 on 2024-01-14 20:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fak_owner", "0012_fakmodels_is_deleted"),
    ]

    operations = [
        migrations.AddField(
            model_name="owner",
            name="mol",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]