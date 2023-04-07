# from django.shortcuts import render
# from rest_framework import generics
# import io, csv, pandas as pd
# from rest_framework.response import Response
# from .Serializer import FileUploadSerializer         
# from core.models import *
# # remember to import the File model
# # remember to import the FileUploadSerializer and SaveFileSerializer

# class UploadFileView(generics.CreateAPIView):
#     serializer_class = FileUploadSerializer
    
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         file = serializer.validated_data['file']
#         reader = pd.read_csv(file)
#         for _, row in reader.iterrows():
#             new_file = File(
#                     #   id = row['Id'],
#                        staff_name= row["staff_name"],
#                        position= row['position'],
#                        age= row["age"],
#                        year_joined= row["year_joined"]
#                        )
#             new_file.save()
#         return Response({"status": "success"},
#                         status.HTTP_201_CREATED)

from django.shortcuts import render
from rest_framework import generics
import  pandas as pd
import csv
from rest_framework.response import Response
from .Serializer import FileUploadSerializer         
from core.models import *
# from import upload-file.csv

# remember to import the File model
# remember to import the FileUploadSerializer and SaveFileSerializer

class upload_file(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        new_file= ["Staff Name", "Designated Position", "Age", "Year Joined"]
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = File(
                       id = request.data.get(id),
                       staff_name= row["Staff Name"],
                       position= row['Designated Position'],
                       age= row["Age"],
                       year_joined= row["Year Joined"]
                       )
            new_file.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)                 