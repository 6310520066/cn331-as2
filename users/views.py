from imp import is_builtin
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, OrderForm

# Create your views here.
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Successful you can login as username: ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'users/register.html', context)

def loginPage(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Username or Password is incorrect.")
    
    context = {}
    return render(request, 'users/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request, message=None):
    user = User.objects.get(id=request.user.id)
    orders = Order.objects.filter(user=user)
    context = {'orders':orders, "err_message": message}
    return render(request, 'users/dashboard.html' )

@login_required(login_url='login')
def all_course(request):
    course = Course.objects.all()
    total = Course.objects.all()
    return render(request, 'users/all_course.html', {'course' :course})

@login_required(login_url='login')
def user(request):
    return render(request, 'users/user.html')

@login_required(login_url='login')
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

@login_required(login_url='login')
def delete_enrollment(request, order_id):
    try:
        print("<--------------- Delete method --------------->")
        print("Order ID : ", order_id)
        # student = User.objects.get(id=request.user.id)
        # course = Course.objects.get(id=course_id)
        # print("Course : ", course)
        # print("Student : ", student)
        order = Order.objects.get(id=order_id)
        print("Order data : ", order)
        order.delete()
        print("Delete successfully !!")
        # return render(request, 'users/delete.html')
        return home(request)
    except Exception as e:
        print("Error : ", e)
    return home(request, {"err_message": "Order not found"})
    # return render(request, "users/index.  html")
