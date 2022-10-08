from venv import create
from django.urls import path, include
from . import views


app_name = "users"

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('home/', views.home, name = "home"),
    path('all_course/', views.all_course, name = "all_course"),
    path('user/', views.user, name = "user"),
    path('create_enrollment/', views.create_enrollment, name="create_enrollment"),
    path('delete_enrollment/<int:order_id>/', views.delete_enrollment, name="delete_enrollment"),
    path('full/', views.full, name="full"),
    path('close/', views.close, name="close"),
]
