# Generated by Django 2.2.1 on 2019-07-13 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0010_auto_20190713_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='pub_date',
            field=models.DateField(auto_now=True),
        ),
    ]
