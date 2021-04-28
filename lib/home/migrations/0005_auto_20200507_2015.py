# Generated by Django 3.0.5 on 2020-05-07 14:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0004_auto_20200507_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='last_borrowed',
            field=models.DateField(default=datetime.datetime(2020, 5, 7, 14, 45, 23, 701179, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lend',
            name='issue_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 7, 14, 45, 23, 752045, tzinfo=utc)),
        ),
    ]
