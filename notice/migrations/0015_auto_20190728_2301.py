# Generated by Django 2.2.1 on 2019-07-28 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0014_auto_20190728_2258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notice',
            options={'ordering': ['-id']},
        ),
    ]
