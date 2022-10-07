from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Course, Order


class UsersTestCase(TestCase):

	def setUp(self):

		# create courses
		course1 = Course.objects.create(course_num = "CN200", maxSeat = 2, state = True)
		# course2 = Course.objects.create(course_num = "CN210", maxSeat = 2, state = False)
		
		Order.objects.create(
			course = course1) #course2 = course2 )
		
	def test_seat_available(self):
		""" is_seat_available should be True """
		cn200 = Course.objects.first()
		raw_course = Course.objects.all()
		course = [model for model in (Course.objects.all().values())]
		for c in range(len(raw_course)):
			orders = Order.objects.filter(course=raw_course[c].id)
			course[c]["seat"] = (len(orders))
   
		self.assertTrue( len(course) < cn200.maxSeat )

	def test_seat_not_available(self):
		""" is_seat_available should be False """
		cn200 = Course.objects.first()
		raw_course = Course.objects.all()
		course = [model for model in (Course.objects.all().values())]
		for c in range(len(raw_course)):
			orders = Order.objects.filter(course=raw_course[c].id)
			course[c]["seat"] = (len(orders))

		# user1 = Order.objects.create(
		# 	first="harry", last="potter")
		# user2 = Order.objects.create(
		# 	first="hermione", last="granger")

		# course =Course.objects.first()
		# course.orders.add(user1)
		# course.orders.add(user2)
		self.assertFalse( len(course) > cn200.maxSeat )
		# self.assertFalse(course.is_seat_available())
	
	# def check_course_status(self):
	#     pass