# Generated by Django 2.2.1 on 2019-07-12 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0006_auto_20190711_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='file',
        ),
    ]
