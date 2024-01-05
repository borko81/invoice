# Generated by Django 5.0 on 2024-01-05 19:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("client_name", models.CharField(max_length=52)),
                ("town", models.CharField(blank=True, max_length=32, null=True)),
                ("address", models.CharField(max_length=32)),
                ("bulstat", models.CharField(max_length=9)),
                ("id_nomer", models.CharField(blank=True, max_length=11, null=True)),
                ("mol", models.CharField(max_length=72)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("telephone", models.CharField(blank=True, max_length=15, null=True)),
                ("comemnt", models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="OwnerBank",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("banka_name", models.CharField(max_length=52)),
                (
                    "banka_name_lat",
                    models.CharField(blank=True, max_length=52, null=True),
                ),
                ("kod", models.CharField(max_length=12)),
                ("smetka", models.CharField(max_length=52)),
                ("last_fak_number", models.CharField(default="0", max_length=10)),
                ("last_pr_number", models.CharField(default="0", max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Owner",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=52)),
                (
                    "full_name_lat",
                    models.CharField(blank=True, max_length=52, null=True),
                ),
                ("town", models.CharField(blank=True, max_length=32, null=True)),
                ("town_lat", models.CharField(max_length=32)),
                ("address", models.CharField(max_length=32)),
                ("address_lat", models.CharField(blank=True, max_length=32, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("telephone", models.CharField(blank=True, max_length=15, null=True)),
                ("bulstat", models.CharField(max_length=9)),
                ("id_nomer", models.CharField(blank=True, max_length=11, null=True)),
                ("url", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "image",
                    models.ImageField(default="default.jpg", upload_to="owner_picture"),
                ),
                (
                    "owner_banka",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="fak_owner.ownerbank",
                    ),
                ),
            ],
        ),
    ]
