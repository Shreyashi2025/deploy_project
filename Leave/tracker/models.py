from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profileinfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    secondname = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)

    def __str__(self):
     return self.user.username
    

class leave(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   start = models.CharField(max_length=100)
   end = models.CharField(max_length=100)
   type = models.CharField(max_length=100)
   reason = models.CharField(max_length=1000)
   action = models.BooleanField(default=False)

   def __str__(self):
      return self.user.username