# Generated by Django 4.1.5 on 2023-03-06 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]
