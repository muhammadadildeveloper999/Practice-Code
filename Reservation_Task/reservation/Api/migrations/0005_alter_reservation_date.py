# Generated by Django 4.1.3 on 2022-11-08 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Api", "0004_alter_reservation_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reservation",
            name="date",
            field=models.DateField(verbose_name="YY/MM/DD"),
        ),
    ]
