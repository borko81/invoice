# Generated by Django 5.0 on 2024-01-05 19:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fak_owner", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="bulstat",
            field=models.CharField(max_length=9, unique=True),
        ),
    ]
