import email
from platform import python_branch
from django.db import models
from datetime import datetime
# Create your models here.
now = datetime.now()
time_sting = now.strftime("%H:%M:%S")
dt_sting = now.strftime("%Y-%m-%d")


class newuser(models.Model):
    name=models.CharField(max_length=20)
    email= models.EmailField(max_length= 50)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=20)