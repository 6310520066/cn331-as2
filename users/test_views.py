from itertools import count
from urllib import response
from django.test import TestCase, Client, SimpleTestCase
from django.urls import reverse, resolve
from django.db.models import Max
from django.contrib.auth.models import User
from ast import arg
from .forms import *
from django.contrib.messages import get_messages
from django.http import HttpResponse
from users.views import home

# Create your tests here.
from .models import Course, Order

class testView(TestCase):
	def setUp(self):
		User.objects.create(username="test", password="test")
		Course.objects.create(course_num = "CN200", maxSeat = 2, state = True)
		Course.objects.create(course_num = "CN210", maxSeat = 0, state = True)

		Order.objects.create(user = User.objects.first())
	
	def test_login_successful(self):
		self.client = Client()
		response = self.client.post(reverse('login'), {"username": "test", "password" : "test"})
		self.assertEqual(response.status_code, 200)

	def test_login_fail(self):
		c = Client()
		response = c.post(reverse('users:login'), {"username": "student", "password" : "student"})
		self.assertEqual(response.status_code, 200)

		response = c.get(reverse('login'))
		self.assertEqual(response.status_code, 200)

		response = c.get(reverse('home'))
		self.assertEqual(response.status_code, 302)
	
	def test_logout_successful(self):
		self.client = Client()
		response = self.client.post(reverse('users:login'), {"username" : "test", "password" : "test"})
		response = self.client.get(reverse('logout'))
		self.assertEqual(response.status_code, 302)

	def test_duplicate_enrollment(self):
		subject = Course.objects.first()
		student = Order.objects.first()

		form = OrderForm()
		if form.is_valid():
			is_registered = Order.objects.filter(user=student.id).filter(course=subject.id)
			if(len(is_registered) > 0):
				response = self.client.get(reverse(HttpResponse("Already registered")))
				self.assertEqual(response.status_code, 200)
	
	
	def test_login_as_admin(self):
		admin = User.objects.create_user(username="admin", password="admin", is_superuser=True)
		login = self.client.login(username="admin", password="admin")
		response = self.client.get(reverse('users:home'))
		self.assertEqual(response.status_code, 200)
