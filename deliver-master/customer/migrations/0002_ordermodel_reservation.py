# Generated by Django 4.2.5 on 2023-09-14 08:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customer", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ordermodel",
            name="reservation",
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
