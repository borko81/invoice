# Generated by Django 5.0 on 2024-01-10 20:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fak_owner", "0007_alter_fakmodels_poluchena_ot"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fakmodels",
            name="fak_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
