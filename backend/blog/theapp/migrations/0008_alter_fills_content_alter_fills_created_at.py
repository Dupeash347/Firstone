# Generated by Django 4.2.3 on 2023-08-14 06:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0007_alter_fills_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fills',
            name='content',
            field=models.TextField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='fills',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 8, 14, 12, 10, 33, 753612)),
        ),
    ]