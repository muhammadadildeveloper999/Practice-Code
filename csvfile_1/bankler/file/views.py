import csv
import imp
from urllib import request
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .models import *

class UploadCsv_File(APIView):
      def post (self,request): 

        file = request.FILES.get("file")

        columnFormat = ['fname','lname','contact','adresss']
        convertDataFrame = pd.read_csv(file)
        convertDataFrame = pd.DataFrame(convertDataFrame)

        convertDataFrame.columns = [x.lower() for x in convertDataFrame.columns]
        dataColumns = convertDataFrame.columns


        if list(dataColumns) == columnFormat:

            fname = convertDataFrame[columnFormat[0]]
            lname = convertDataFrame[columnFormat[1]]
            contact = convertDataFrame[columnFormat[2]]
            adresss = convertDataFrame[columnFormat[3]]

            bulklist = list()

            for a,b,c,d in zip(fname,lname,contact,adresss):

                bulklist.append(excel(firstname=a,lastname=b,phone=c,address=d))

            excel.objects.bulk_create(bulklist)
        return HttpResponse({"status": True, "msg":"Added Successfully"})