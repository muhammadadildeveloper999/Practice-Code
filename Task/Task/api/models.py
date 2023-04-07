from django.db import models

# Create your models here.

class Class_name(models.Model):
    Class = models.CharField(max_length=255, default='')
    
    def __str__(self):                                                                                                     
        return self.Class
    
class Student(models.Model):
    name = models.CharField(max_length=100,default="")
    email = models.EmailField(max_length=100,default="")
    # city = models.CharField(max_length=100,default="")
    classid = models.ForeignKey(Class_name,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):                                                                                                     
        return self.name
    