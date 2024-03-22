from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Passwords(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    account=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    
    def __str__(self):
        return self.account