from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm 

# Create your views here.

def home(request, message=None):
    user = User.objects.get(id=request.user.id)
    orders = Order.objects.filter(user=user)
    context = {'orders':orders, "err_message": message}
    return render(request, 'users/dashboard.html', context, )

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