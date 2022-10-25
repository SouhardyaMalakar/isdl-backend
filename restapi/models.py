from django.db import models
from django.contrib.postgres.fields import ArrayField

class Actor(models.Model):
    
    actor_name = models.CharField(max_length=40)
    actor_id = models.AutoField(primary_key=True)
    actor_mail=models.EmailField(max_length=40)
    
    actor_booked = models.ManyToManyField(Hall,through='DateTime')
    actor_pending = models.ManyToManyField(Hall,through='DateTime')

class DateTime(models.Model):
    
    actor = models.ForeignKey(Actor, on_delete=CASCADE)
    hall = models.ForeignKey(Hall, on_delete=CASCADE)
    booked = models.BooleanField()

class Hall(models.Model):
    
    #hall_isreq how to check in time slot?
    #hall_isbooked how to check in time slot?
    
    hall_name = models.CharField(max_length=40)
    hall_id = models.AutoField(primary_key=True)
    hall_location = models.CharField(max_length=40)
    hall_capacity = models.IntegerField()
    hall_rating = models.IntegerField()
    hall_image = models.CharField(max_length=40)

    hall_selectedslots = ArrayField(ArrayField(models.IntegerField())) # [date int, time slot int]

class Requests(models.Model):
    
    req_id = models.AutoField(primary_key=True)
    req_approved = models.BooleanField()