from django.urls import path,re_path
from .views import api_home
urlpatterns = [
    path('home',api_home)
]
