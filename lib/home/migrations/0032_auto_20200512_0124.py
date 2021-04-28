# Generated by Django 3.0.5 on 2020-05-11 19:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0031_auto_20200510_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='last_borrowed',
            field=models.DateField(default=datetime.datetime(2020, 5, 11, 19, 54, 3, 205215, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lendbook',
            name='due_date',
            field=models.DateField(default=datetime.date(2020, 5, 26)),
        ),
        migrations.AlterField(
            model_name='lendbook',
            name='issue_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 11, 19, 54, 3, 206212, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lends',
            name='due_date',
            field=models.DateField(default=datetime.date(2020, 5, 26)),
        ),
        migrations.AlterField(
            model_name='lends',
            name='issue_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 11, 19, 54, 3, 155813, tzinfo=utc)),
        ),
    ]