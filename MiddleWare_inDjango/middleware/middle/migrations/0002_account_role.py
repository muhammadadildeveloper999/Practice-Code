# Generated by Django 4.1 on 2022-08-27 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("middle", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="role",
            field=models.CharField(
                choices=[("admin", "admin"), ("company", "company")],
                default="admin",
                max_length=20,
            ),
        ),
    ]
