from datetime import date
from email.policy import default
from multiprocessing.sharedctypes import Value
from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)

class Messages(models.Model):
    value = models.CharField(max_length=10000)
    user = models.CharField(max_length=10000)
    room = models.CharField(max_length=10000)
    date = models.DateTimeField(default=datetime.now, blank=True)