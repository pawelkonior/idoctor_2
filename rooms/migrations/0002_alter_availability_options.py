# Generated by Django 3.2 on 2021-08-10 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='availability',
            options={'verbose_name': 'Availability', 'verbose_name_plural': 'Availabilities'},
        ),
    ]
