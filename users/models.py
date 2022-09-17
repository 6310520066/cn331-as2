from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    course_num = models.CharField(max_length=5)
    course_name = models.CharField(max_length=64)
    seat = models.IntegerField(null=True)
    maxSeat = models.IntegerField(null=True)
    semester = models.IntegerField(null=True)
    year = models.IntegerField(null=True)
    state = models.BooleanField(default=None)

    def __str__(self):
        return f"{self.course_num} {self.course_name} "
    
class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
    course = models.ForeignKey(Course, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return f"{self.course.course_name} {self.user.id}"
        
        

    