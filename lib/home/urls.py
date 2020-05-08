from django.urls import path
from .views import Home, Lend, Aboutus, Students, post

urlpatterns = [
    path('', Home, name='Home'),
    path('aboutus/', Aboutus, name='Aboutus'),
    path('lend/', Lend, name='lend'),
    path('add_student/', post, name='add_student'),
    path('Students/', Students, name='Students'),
]

