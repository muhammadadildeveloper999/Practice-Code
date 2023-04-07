from django.db import models
from django.db import models

# Create your models here.

class payment(models.Model):
    user = models. CharField(max_length=255 ,default= "")
    amount = models. IntegerField(default= "")
    
    def __str__(self):
        return self.user