# Generated by Django 3.0.5 on 2020-05-01 20:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0002_auto_20200427_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='last_borrowed',
            field=models.DateField(default=datetime.datetime(2020, 5, 1, 20, 2, 19, 165838, tzinfo=utc)),
        ),
    ]
