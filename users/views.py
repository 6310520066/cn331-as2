from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm 

# Create your views here.

def home(request):
    orders = Order.objects.all()
    context = {'orders':orders}
    return render(request, 'users/dashboard.html', context)

def all_course(request):
    course = Course.objects.all()
    total = Course.objects.all()
    return render(request, 'users/all_course.html', {'course' :course})

def user(request):
    return render(request, 'users/user.html')

def create_enrollment(request): 
    
    form = OrderForm()
    if request.method == 'POST':
        #print("Printing POST: ", request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            
            
    context = {'form':form}
    return render(request, 'users/create_enrollment.html', context)