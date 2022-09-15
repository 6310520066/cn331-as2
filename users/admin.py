from django.contrib import admin

# Register your models here.

from .models import Course, Order, User

admin.site.register(Course)
admin.site.register(User)
admin.site.register(Order)
