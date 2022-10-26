from email.policy import default
from enum import auto, unique
from re import T
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

'''
https://www.sankalpjonna.com/learn-django/the-right-way-to-use-a-manytomanyfield-in-django
for future refrence
'''
class Hall(models.Model):
    
    #hall_isreq how to check in time slot?
    #hall_isbooked how to check in time slot?
    
    hall_name = models.CharField(max_length=40)
    id = models.AutoField(primary_key=True)
    hall_location = models.CharField(max_length=40)
    hall_capacity = models.IntegerField()
    hall_rating = models.IntegerField()
    hall_image = models.URLField( max_length=200)

    hall_selectedslots = ArrayField(ArrayField(models.IntegerField())) # [date int, time slot int] #no need we cann acess


class User(AbstractUser):
    
    name = models.CharField(max_length=40)
    # id = models.AutoField(primary_key=True)
    email=models.EmailField(max_length=40,unique=True)
    bookings = models.ManyToManyField(Hall,through='Booking')
    isAdmin=models.BooleanField(default=False)
    username=None
    password=models.CharField(max_length=256)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]

class Booking(models.Model):
    
    actor = models.ForeignKey(User, on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    booked = models.BooleanField()
    pending=models.BooleanField()
    slotStart=models.DateTimeField(null=True,blank=True)
    slotEnd=models.DateTimeField(null=True,blank=True)