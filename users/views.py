from imp import is_builtin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    orders = Order.objects.all()
    context = {'orders':orders}
    return render(request, 'users/dashboard.html', context)

@login_required(login_url='login')
def all_course(request):
    course = Course.objects.all()
    total = Course.objects.all()
    return render(request, 'users/all_course.html', {'course' :course})

@login_required(login_url='login')
def user(request):
    return render(request, 'users/user.html')

def my_course(request):
    return redirect('')