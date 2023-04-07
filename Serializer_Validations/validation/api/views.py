from django.shortcuts import render
# Create your views here.
from.models import Student
from .serializer import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django_filters import rest_framework as filters
from rest_framework import viewsets
from django.http import HttpResponse
from .models import*
import api.usable as uc
from .serializer import* 
from rest_framework import status

# Api_Validation

# post api

class super(APIView):
    def post(self, request):
        requireFields = ['name', 'email', 'password', 'age', 'phone']
        validator = uc.keyValidation(True,True,request.data,requireFields)
        
        if validator:
            return Response(validator,status = 200)
    
        else:    
            serializer = StudentSerializer(data = request.data)

            if int(request.data['age']) < 18:
                return Response({'status':403, 'message':'Age must be greater than 18'})


            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors, 'message':'something went Wrong' })
            
            serializer.save()
            return Response({'status':200, 'message':'your data successfully added'})
        
# get api
    def get(request,self):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs, many=True)
        return Response({'status' : 403 , 'Data' : serializer.data, 'message' : 'Data SUCCESSFULLY GET'})

                                                                          
# update api
    def put(request,self):
        try:

            student_objs = Student.objects.get(id = id)    
            serializer = Student(data = request.data)
        
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status' : 403 , 'error' : serializer.error, 'message' : 'Something Went Wrong'})
               
            serializer.save()    
            return Response({'status' : 403 , 'error' : serializer.error, 'message' : 'Something Went Wrong'})

        except Exception as e:
            print(e)
            return Response({'status' : 403 , 'message' : 'invalid id'})

# delete api
    def delete(self,request):
        try:

            id = request.GET.get("id")
            student_objs = Student.objects.get(id = id)
            student_objs.delete()
            
            return Response({'status' : 200 , 'error' : 'delete success'})

        except Exception as e:
            print(e)
            return Response({'status' : 403 , 'error' : 'invalid id'})


