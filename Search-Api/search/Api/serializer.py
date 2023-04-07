from rest_framework import serializers
from .models import*

class StudentSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Student
        fields = '__all__'
        fields = ['name', 'email', 'city',]             