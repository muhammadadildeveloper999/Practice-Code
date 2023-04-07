from django.db import models

class File(models.Model):
    
    id = models.CharField(primary_key=True, max_length=6)
    staff_name = models.CharField(max_length=100, default="")
    position = models.CharField(max_length=200, default="")
    age = models.IntegerField()
    year_joined = models.CharField(max_length=4, default="")
    
    def __str__(self):
        return self.staff_name