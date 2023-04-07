from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=255, default="")

class Salary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='salary')