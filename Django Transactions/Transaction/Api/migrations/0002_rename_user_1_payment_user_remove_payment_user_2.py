# Generated by Django 4.1.6 on 2023-02-02 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='user_1',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user_2',
        ),
    ]
