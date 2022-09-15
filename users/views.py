from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm 

# Create your views here.

def home(request):
    return render(request, 'users/dashboard.html')

def all_course(request):
    course = Course.objects.all()
    total = Course.objects.all()
    return render(request, 'users/all_course.html', {'course' :course})

def user(request):
    return render(request, 'users/user.html')

def create_enrollment(request): 
    
    form = OrderForm()
    
    context = {'form':form}
    return render(request, 'users/create_enrollment.html', context)