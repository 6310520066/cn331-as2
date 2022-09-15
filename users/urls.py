from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('all_course/', views.all_course),
    path('user/', views.user),

]
