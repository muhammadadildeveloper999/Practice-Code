# Generated by Django 4.0.5 on 2022-07-14 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='super_adminacount',
            old_name='SId',
            new_name='Id',
        ),
    ]
