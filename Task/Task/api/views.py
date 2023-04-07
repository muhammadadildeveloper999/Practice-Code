from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from django.db.models import F

class Stu_Class_Get(APIView):
   def get(self, request):

      data = Class_name.objects.all().values('id','Class')

      for i in range(len(data)):

         student_data = Student.objects.all().values('id','name','email')
          
         for j in range(len(data)):

          if  data:         
              data[i]['student_data'] = student_data
              
          else:
            data[i]['Student'] =''

      return Response({"status":True,'data':data,})


   
# class Stu_Class_Get(APIView):
#       def get(self,request):
#             id = request.GET['id']
            
#             data = Class_name.objects.filter(id=id).values('id','Class')
            
#             for i in range(len(data)):

#                 student_data = Student.objects.filter(classid__id=data[i]['id']).values('id','name','email')

#                 if student_data:
                                                                    
#                     imagelist = []
#                     for j in range(len(student_data)):
                        
#                         imagelist.append(student_data[j]['name'])
#                         data[i]['Class_name'] = imagelist
#                 else:
#                     data[i]['Student'] =''

#             return Response({"status":True,'data':data})