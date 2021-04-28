from django.contrib import admin
from .models import books, Student, lendbook, lends

# Register your models here.


admin.site.register(Student)
admin.site.register(books)
admin.site.register(lendbook)
admin.site.register(lends)
