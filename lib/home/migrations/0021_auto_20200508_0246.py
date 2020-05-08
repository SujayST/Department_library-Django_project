# Generated by Django 3.0.5 on 2020-05-07 21:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20200508_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='last_borrowed',
            field=models.DateField(default=datetime.datetime(2020, 5, 7, 21, 16, 23, 811601, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lend',
            name='issue_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 7, 21, 16, 23, 876429, tzinfo=utc)),
        ),
    ]
