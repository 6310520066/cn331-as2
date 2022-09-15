from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('all_course/', views.all_course, name = "all_course"),
    path('user/', views.user, name = "user"),

]
