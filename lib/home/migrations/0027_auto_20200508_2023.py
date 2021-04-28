# Generated by Django 3.0.5 on 2020-05-08 14:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('home', '0026_auto_20200508_2017'),
    ]

    operations = [
        migrations.CreateModel(
            name='lendbook',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('USNn', models.CharField(max_length=12)),
                ('book_id', models.CharField(max_length=5)),
                ('issue_date', models.DateField(default=datetime.datetime(2020, 5, 8, 14, 53, 54, 821062, tzinfo=utc))),
                ('due_date', models.DateField(default=datetime.date(2020, 5, 23))),
            ],
        ),
        migrations.DeleteModel(
            name='lend',
        ),
        migrations.AlterField(
            model_name='books',
            name='last_borrowed',
            field=models.DateField(default=datetime.datetime(2020, 5, 8, 14, 53, 54, 740276, tzinfo=utc)),
        ),
    ]
