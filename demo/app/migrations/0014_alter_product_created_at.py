# Generated by Django 3.2.6 on 2022-02-25 15:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20220225_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 25, 15, 4, 53, 192381, tzinfo=utc), verbose_name='Дата создания'),
        ),
    ]