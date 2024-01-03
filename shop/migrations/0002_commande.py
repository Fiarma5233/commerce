# Generated by Django 5.0 on 2024-01-03 02:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Commande",
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
                ("items", models.CharField(max_length=400)),
                ("nom", models.CharField(max_length=200)),
                ("tel", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("addresse", models.CharField(max_length=200)),
                ("ville", models.CharField(max_length=200)),
                ("pays", models.CharField(max_length=200)),
                ("zipcode", models.CharField(max_length=200)),
                ("date_commande", models.DateTimeField(auto_now=True)),
            ],
            options={
                "ordering": ["date_commande"],
            },
        ),
    ]
