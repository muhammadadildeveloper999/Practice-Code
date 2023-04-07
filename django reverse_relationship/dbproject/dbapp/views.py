from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from .models import*

class resverse_relationship(APIView):
    def post(self, request):
        name = request.data.get("name")
        employee = request.data.get("employee")          
            
        newemployeeget = Employee.objects.filter(id=employee).first() 

        data = Salary(employee=newemployeeget)
        data = Employee(name=name)                              

        data.save()

        return Response({"status":True, "Msg":"JHFHGF"},201)
       




                                                                                                                                                                                                                                 