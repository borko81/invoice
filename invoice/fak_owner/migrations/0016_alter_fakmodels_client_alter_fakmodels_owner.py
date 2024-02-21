# Generated by Django 5.0 on 2024-02-21 16:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fak_owner", "0015_remove_ownerbank_last_fak_number_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fakmodels",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="fak_owner.client"
            ),
        ),
        migrations.AlterField(
            model_name="fakmodels",
            name="owner",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="fak_owner.owner",
            ),
        ),
    ]