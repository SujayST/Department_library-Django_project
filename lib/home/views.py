from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import lendbook, Student, books
from .forms import *
from django.utils import timezone
import datetime


# Create your views here.
def Home(request):

    all_books = books.objects.all()

    context = {
        'all_books': all_books
    }

    return render(request, 'home.html', context)


def Students(request):

    allvideos = Student.objects.all()
    obj = Student.objects.get(USN='01fe18bcs226')
    context = {
        "data": obj,
        'allvideos': allvideos
    }
    return render(request, 'students.html', context)


def Lend(request):

    if request.method == "POST":
        form = lendForm(request.POST)

        if form.is_valid():
            trn = lendbook()
            trn.USN = form.cleaned_data["USN"]
            trn.book_id = form.cleaned_data["book_id"]
            trn.issue_date = form.cleaned_data["issue"]
            trn.due_date = form.cleaned_data["due"]
            trn.save()

    else:
        form = lendForm()

    return render(request, 'lendBook.html', locals())


def post(request):

    if request.method == "POST":
        form = addForm(request.POST)
        if form.is_valid():
            student = Student()
            student.USN = form.cleaned_data["USN"]
            student.Name = form.cleaned_data["Name"]
            student.Semester = form.cleaned_data["Semester"]
            student.phone_no = form.cleaned_data["phone_no"]
            student.save()
    else:
        form = addForm()

    return render(request, 'add_student.html', locals())


def Aboutus(request):
    return render(request, 'contact.html')
