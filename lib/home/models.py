from django.db import models
from django.utils import timezone
import datetime


# Create your models here.


class lends(models.Model):
    transaction_id = models.AutoField(primary_key=True, serialize=True)
    USN = models.CharField(max_length=12)
    book_id = models.CharField(max_length=5)
    issue_date = models.DateField(default=timezone.now())
    return_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.USN


class books(models.Model):
    book_id = models.IntegerField(primary_key=True, serialize=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=15)
    No_of_Copies = models.CharField(max_length=9)
    last_borrowed = models.DateField(default=timezone.now())

    def __str__(self):
        return self.title


class Student(models.Model):
    USN = models.CharField(max_length=12, primary_key=True, serialize=True)
    Name = models.CharField(max_length=30)
    Semester = models.CharField(max_length=5)
    phone_no = models.BigIntegerField(unique=True)

    def __str__(self):
        return self.Name


class lendbook(models.Model):
    transaction_id = models.AutoField(primary_key=True, serialize=True)
    USNn = models.CharField(max_length=12)
    book_id = models.CharField(max_length=5)
    issue_date = models.DateField(default=timezone.now())
    due_date = models.DateField(default=timezone.now().date() + datetime.timedelta(days=15))

    def __str__(self):
        return self.USNn
