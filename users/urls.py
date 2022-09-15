from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('all_course/', views.all_course, name = "all_course"),
    path('user/', views.user, name = "user"),
    path('create_enrollment/', views.create_enrollment, name="create_enrollment")
]
