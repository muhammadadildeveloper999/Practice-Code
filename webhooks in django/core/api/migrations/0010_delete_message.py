# Generated by Django 4.1.7 on 2023-03-06 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_message_text'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
