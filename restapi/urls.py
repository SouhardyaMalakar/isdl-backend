from django.urls import path,re_path
from .views import api_home, logout,register,login, userView
from .user_views import createBooking
urlpatterns = [
    path('home',api_home),
    path('register',register),
    path('login',login),
    path('user',userView),
    path('logout',logout),
    path('createBooking',createBooking)
]
