from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response
from Api.models import *

# class employees(APIView):
#       def post(self, request):
#             name = request.data.get("name")
#             email = request.data.get("email")
#             city = request.data.get("city")
    
#             data = employee(name=name,email=email,city=city)
#             data.save()

#             return Response({'status':True, 'Msg': "Post successfully"})
         
class search_field(APIView):
    def get(self, request):
        data = employee.objects.filter(city__icontains='karachi').values('city')
    
        return Response({'status':True, 'data':data})

