# Generated by Django 3.2.18 on 2023-04-26 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configurator', '0017_auto_20230426_1758'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cooling',
            old_name='type',
            new_name='cooling_type',
        ),
        migrations.RenameField(
            model_name='powersupplyunit',
            old_name='power',
            new_name='psu_power',
        ),
    ]
