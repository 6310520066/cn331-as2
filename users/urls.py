from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('all_course/', views.all_course, name = "all_course"),
    path('user/', views.user, name = "user"),
    path('create_enrollment/', views.create_enrollment, name="create_enrollment"),
    path('delete_enrollment/<int:order_id>/', views.delete_enrollment, name="delete_enrollment")
]
