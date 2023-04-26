# Generated by Django 3.2.18 on 2023-04-25 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurator', '0014_auto_20230425_2317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housing',
            name='height',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='length',
        ),
        migrations.RemoveField(
            model_name='housing',
            name='width',
        ),
        migrations.AddField(
            model_name='housing',
            name='dimensions',
            field=models.CharField(blank=True, help_text='(WxHxD) in cm', max_length=15, null=True),
        ),
    ]
