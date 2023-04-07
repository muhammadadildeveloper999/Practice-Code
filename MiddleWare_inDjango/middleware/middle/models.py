from django.db import models


role={
    ('admin','admin'),
    ('company','company'),
}


class account(models.Model):
    firstname=models.CharField(max_length=255, default='')
    lastname=models.CharField(max_length=255, default='')
    address=models.CharField(max_length=255, default='')
    email=models.EmailField(max_length=255, default='')
    password=models.CharField(max_length=255, default='')
    phone=models.CharField(max_length=255, default='')
    role=models.CharField(choices=role,max_length=20,default="admin")

    
    def __str__(self):
        return self.firstname
 

class employee(models.Model):
    firstname=models.CharField(max_length=255, default='')
    lastname=models.CharField(max_length=255, default='')
    address=models.CharField(max_length=255, default='')
    email=models.EmailField(max_length=255, default='')
    password=models.CharField(max_length=255, default='')
    phone=models.CharField(max_length=255, default='')

    
    def __str__(self):
        return self.firstname
    
