# Generated by Django 4.1.3 on 2022-11-27 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("name", models.CharField(max_length=100, null=True)),
                ("email", models.EmailField(max_length=100, null=True)),
                ("phone_number", models.CharField(max_length=15, null=True)),
                ("massage", models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
