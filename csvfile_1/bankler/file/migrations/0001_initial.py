# Generated by Django 4.0.6 on 2022-08-02 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='excel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='', max_length=255)),
                ('lastname', models.CharField(default='', max_length=255)),
                ('phone', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
