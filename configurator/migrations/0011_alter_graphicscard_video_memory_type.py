# Generated by Django 3.2.18 on 2023-04-25 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurator', '0010_alter_graphicscard_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphicscard',
            name='video_memory_type',
            field=models.CharField(max_length=6),
        ),
    ]
