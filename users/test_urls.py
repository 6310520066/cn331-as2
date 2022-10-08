from distutils.core import setup
from django.test import TestCase
from django.urls import reverse, resolve
from users.views import *

class TestUrls(TestCase):
	# def setUp(self):
	# 	course1 = Course.objects.create(course_num = "CN200", maxSeat = 2, state = True)
	# 	order1 = Order.objects.create(course = course1)
  
	def test_register_url_is_resolved(self):
		url = reverse("users:register")
		print(resolve(url))
		self.assertEquals(resolve(url).func, registerPage)
		
	def test_login_url_is_resolved(self):
		url = reverse("users:login")
		print(resolve(url))
		self.assertEquals(resolve(url).func, loginPage)
		
	def test_logout_url_is_resolved(self):
		url = reverse("users:logout")
		print(resolve(url))
		self.assertEquals(resolve(url).func, logoutUser)
  
	def test_home_url_is_resolved(self):
		url = reverse("users:home")
		print(resolve(url))
		self.assertEquals(resolve(url).func, home)
  
	def test_all_course_url_is_resolved(self):
		url = reverse("users:all_course")
		print(resolve(url))
		self.assertEquals(resolve(url).func, all_course)
  
	def test_user_is_resolved(self):
		url = reverse("users:user")
		print(resolve(url))
		self.assertEquals(resolve(url).func, user)
  
	def test_create_enrollment_is_resolved(self):
		url = reverse("users:create_enrollment")
		print(resolve(url))
		self.assertEquals(resolve(url).func, create_enrollment)
	
	def test_delete_enrollment_is_resolved(self):
		url = reverse("users:delete_enrollment", args = [1])
		print(resolve(url))
		self.assertEquals(resolve(url).func, delete_enrollment)
 
	def test_full_is_resolved(self):
		url = reverse("users:full")
		print(resolve(url))
		self.assertEquals(resolve(url).func, full)
	
	def test_close_is_resolved(self):
		url = reverse("users:close")
		print(resolve(url))
		self.assertEquals(resolve(url).func, close)
