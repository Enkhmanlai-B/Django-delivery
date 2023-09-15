# Generated by Django 4.2.5 on 2023-09-14 07:24

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OrderModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(blank=True, max_length=50)),
                ("table_number", models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
