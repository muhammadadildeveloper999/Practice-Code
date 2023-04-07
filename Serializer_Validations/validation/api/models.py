from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100,default="")
    age = models.CharField(max_length=100,default="")
    email = models.EmailField(max_length=100,default="")
    password = models.CharField(max_length=100,default="")
    phone = models.CharField(max_length=100,default="")
