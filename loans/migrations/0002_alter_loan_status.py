# Generated by Django 4.1 on 2022-08-15 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("loans", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loan",
            name="status",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "accepted"), (2, "pending"), (3, "rejected")], default=2
            ),
        ),
    ]