from django.contrib import admin

# Register your models here.
from .models import Student

# @admin.register(Student)

@admin.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'password', 'phone', 'email']
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name','rollnumber', 'city', 'mark', 'grade', 'age', 'password', 'phone', 'email']