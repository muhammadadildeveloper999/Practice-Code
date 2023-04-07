from django.db import models

# Create your models here.
class account(models.Model):
    firstname = models.CharField(max_length=255, default="")
    lastname = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=255,default="")
    email = models.EmailField(default="")
    password = models.CharField(max_length=255,default="")
    