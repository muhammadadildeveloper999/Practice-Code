from django.shortcuts import render
# Create your views here.
from.models import*
from .serializer import*
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .models import*
from .serializer import* 



# class verification(APIView):
#     def post(self, request, *args, **kwargs):
#         # uv = UserVote(created_by=self.request.user)
#         # serializer = UserVoteSerializer(uv, data=request.data)
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# # Serializer_Introduction?
# def Student_data(request):
#     student = Student.objects.get(id = 1)
#     # print(student)
#     serializer= StudentSerialzer(student)
#     # print(serializer)
#     # print(serializer.data)
#     json_data = JSONRenderer().render(serializer.data)
#     # print(json_data)
    
#     #  return HttpResponse(json_data , content_type='application/json')  
#     return JsonResponse(serializer.data, safe=True)

# # Query_set All Student_data 
# def Student_list(request):
#     student = Student.objects.all()
#     # print(student)
#     serializer= StudentSerialzer(student, many=True)
#     # print(serializer)
#     # print(serializer.data)
#     json_data = JSONRenderer().render(serializer.data)
#     # print(json_data)
    # return HttpResponse(json_data , content_type='application/json')  


