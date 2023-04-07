from django.db import models

# Create your models here.
class excel (models.Model):
    firstname=models.CharField(max_length=255, default="") 
    lastname=models.CharField(max_length=255, default="") 
    phone=models.CharField(max_length=100, default="")
    address=models.CharField(max_length=255, default="") 
    
    def __str__(self):
        return self.firstname


