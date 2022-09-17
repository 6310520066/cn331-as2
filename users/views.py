from users.forms import OrderForm
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import CreateUserForm

# Create your views here.
@login_required(login_url='login')	
def home(request, message=None):
	user = User.objects.get(pk=request.user.id)
	orders = Order.objects.filter(user=user)
	context = {'orders':orders, "err_message": message}
	return render(request, 'users/dashboard.html', context, )

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
def all_course(request):
	raw_course = Course.objects.all()
	course = [model for model in (Course.objects.all().values())]

	for c in range(len(raw_course)):
		orders = Order.objects.filter(course=raw_course[c].id)
		course[c]["seat"] = (len(orders))
	
	return render(request, 'users/all_course.html', {'course': (course)}, )

@login_required(login_url='login')
def user(request):
	return render(request, 'users/user.html')

@login_required(login_url='login')
def create_enrollment(request): 
	
	form = OrderForm()
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			is_registered = Order.objects.filter(user=request.user.id).filter(course=request.POST["course"])
			if(len(is_registered) > 0):
				return HttpResponse("Already registered")
			course= Course.objects.get(pk=int(request.POST['course']))
			seat = course.seat
			maxSeat = course.maxSeat
			if(seat >= maxSeat):
				return redirect('full')
			if(not course.state):
				return redirect('close')
			order = form.save()
			user_instance = User.objects.get(pk=request.user.id)
			order.user = user_instance
			order.save()
			return redirect('/')
				
	context = {'form':form}
	return render(request, 'users/create_enrollment.html', context)

@login_required(login_url='login')
def delete_enrollment(request, order_id):
	try:
		print("<--------------- Delete method --------------->")
		print("Order ID : ", order_id)
  
		order = Order.objects.get(id=order_id)
		print("Order data : ", order)
		order.delete()
		print("Delete successfully !!")
		return home(request)
	except Exception as e:
		print("Error : ", e)
	return home(request, {"err_message": "Order not found"})


def registerPage(request):
	if(request.user.is_authenticated):
		return redirect('home')
	else:
		form = CreateUserForm()
		if(request.method == 'POST'):
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Successful you can login as username: ' + user)
				return redirect('login')
			
		context = {'form':form}
		return render(request, 'users/register.html', context)

@login_required(login_url='login')
def full(request):
	return render(request, 'users/full.html')

@login_required(login_url='login')
def close(request):
	return render(request, 'users/close.html')
