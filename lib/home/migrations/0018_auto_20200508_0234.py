# Generated by Django 3.0.5 on 2020-05-07 21:04

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0017_auto_20200508_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='last_borrowed',
            field=models.DateField(default=datetime.datetime(2020, 5, 7, 21, 4, 34, 139143, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='lend',
            name='USN',
            field=models.ForeignKey(max_length=12, on_delete=django.db.models.deletion.CASCADE, to='home.Student'),
        ),
        migrations.AlterField(
            model_name='lend',
            name='issue_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 7, 21, 4, 34, 191005, tzinfo=utc)),
        ),
    ]
