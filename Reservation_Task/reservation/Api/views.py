# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from django.db.models import Sum
from operator import*
import  Api.usable as uc
import calendar
# import fake 
# from fake.providers import BaseProvider

class Reservation_get(APIView):
   def get(self, request):
           
        # monthlist = ['jan','feb','mr','april','may','june','july','august','sep','oct','nov','dec']   

        data = reservation.objects.values('date__month' , 'date__year' ).annotate(Sale=Sum('amount')).order_by()        
        initial = 0
        for i in data:           
                month = calendar.month_name[data[initial]['date__month']]
                data[initial]['datemonth'] = month
                initial =+1
         
        # month = data[0]['date__month']
         
        # getmonth =  monthlist[month]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        return Response({"status":True, 'data' : data})                                                                                                                                                                                                                                                                                            
                
