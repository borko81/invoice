# Generated by Django 5.0 on 2024-01-06 16:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("fak_owner", "0002_alter_client_bulstat"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="client",
            options={"ordering": ["client_name"]},
        ),
    ]