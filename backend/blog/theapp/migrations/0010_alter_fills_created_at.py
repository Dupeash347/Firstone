# Generated by Django 4.2.4 on 2023-08-28 06:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0009_alter_fills_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fills',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 28, 12, 10, 43, 691548)),
        ),
    ]