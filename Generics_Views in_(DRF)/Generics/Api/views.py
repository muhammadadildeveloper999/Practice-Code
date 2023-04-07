from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from.models import Student
from .models import*
from .serializers import* 


class genericsstudent(generics.ListAPIView,generics.CreateAPIView):
       queryset = Student.objects.all()
       serializer_class = StudentSerializer




class StudentGenerics(generics.UpdateAPIView , generics.DestroyAPIView):
       queryset = Student.objects.all()
       serializer_class = StudentSerializer
       lookup_fields = 'id'
