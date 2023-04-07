from django.db import models

class employee(models.Model):
    name=models.CharField(max_length=255, default='')
    email=models.CharField(max_length=255, default='')
    city=models.CharField(max_length=255, default='')

    
    def __str__(self):
        return self.name