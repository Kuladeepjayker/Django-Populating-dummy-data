# Generated by Django 3.0.6 on 2020-07-03 10:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FThrottle', '0004_auto_20200703_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 7, 3, 15, 58, 20, 389235)),
        ),
    ]