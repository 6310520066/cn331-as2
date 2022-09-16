from django.contrib import admin

# Register your models here.

from .models import Course, Order


admin.site.register(Course)
admin.site.register(Order)
