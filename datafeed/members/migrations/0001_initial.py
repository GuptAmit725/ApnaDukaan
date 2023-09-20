# Generated by Django 4.2.5 on 2023-09-19 17:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
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
                ("name", models.CharField(max_length=255)),
                ("place", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=10)),
                ("amt_pur", models.IntegerField()),
                ("on_or_of", models.CharField(max_length=3)),
                ("date", models.DateField()),
            ],
        ),
    ]