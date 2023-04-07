from django.db import models

# Create your models here.

class reservation(models.Model):
    date = models.DateField('%d %b, %y')    
    amount=models.IntegerField(max_length=255, default='')
    name=models.CharField(max_length=255, default='')
    customer_id=models.CharField(max_length=255, default='')

    
    def __str__(self):                                                                                                     
        return self.name
