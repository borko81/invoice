# Generated by Django 5.0 on 2024-01-11 21:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fak_owner", "0011_fakmodels_pay_tip"),
    ]

    operations = [
        migrations.AddField(
            model_name="fakmodels",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
    ]