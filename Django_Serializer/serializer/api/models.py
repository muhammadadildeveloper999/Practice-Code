from django.db import models

# class UserVote(models.Model):
#     created_by = models.CharField(max_length=100,default="")
#     rating = models.CharField(max_length=100,default="")


#     class Meta:
#         unique_together = ('created_by', 'rating')

class Student(models.Model):
    name = models.CharField(max_length=100,default="")
    rollno = models.CharField(max_length=100,default="")
    marks = models.CharField(max_length=100,default="")
    grade = models.CharField(max_length=100,default="")
    age = models.CharField(max_length=100,default="")
    email = models.EmailField(max_length=100,default="")
    password = models.CharField(max_length=100,default="")
    phone = models.CharField(max_length=100,default="")


