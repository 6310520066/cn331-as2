from email.policy import default
from unittest.mock import seal
from django.db import models

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
        return f"{self.id}. Course: {self.course_num} {self.course_name} seat: {self.seat}/{self.maxSeat}"
    
    def availableSeat(self):
        return self.maxSeat-self.seat
    
