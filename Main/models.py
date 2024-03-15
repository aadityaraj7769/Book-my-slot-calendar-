from django.db import models
from django.contrib.auth.models import User
from django.apps import apps

# Create your models here.

# AdminUsers = apps.get_model('Main', 'AdminUsers')

class Calendar(models.Model): #all calendars
    name = models.CharField(max_length=255)
    description = models.TextField(default='')
    users = models.ManyToManyField(User, through='UserCalendar')

class Event(models.Model):
    title = models.CharField(max_length=255)
    date_and_time = models.DateTimeField()
    duration = models.IntegerField(default=10)
    venue = models.CharField(max_length=255, default= '')

    def date(self):
        return self.date_and_time.date()
    
    def time(self):
        return self.date_and_time.time()
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)

class UserCalendar(models.Model): #calenders that are created by user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    calendar = models.ForeignKey(Calendar, on_delete=models.CASCADE)
