from django.db import models

# Create your models here.

class Student(models.Model):
    firstname=models.CharField(max_length=255, default='')
    email=models.EmailField(max_length=255, default='')
    password=models.CharField(max_length=255, default='')
    contact=models.CharField(max_length=255, default='')
    
    def __str__(self):
        return self.firstname
 