# Generated by Django 4.2.5 on 2023-09-14 08:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customer", "0003_menuitem"),
    ]

    operations = [
        migrations.AddField(
            model_name="menuitem",
            name="title",
            field=models.CharField(blank=True, max_length=50),
        ),
    ]