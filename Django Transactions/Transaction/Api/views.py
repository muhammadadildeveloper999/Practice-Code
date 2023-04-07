from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.db import transaction
# Create your views here.
class Home(APIView):
    def post(self,request):
        try:
            user_1 = request.data.get('user_1')
            user_2 = request.data.get('user_2')
            amount = request.data.get('amount')
            with transaction.atomic():
                user_obj_1 = payment.objects.get(user = user_1)
                user_obj_1.amount -= int(amount)
                user_obj_1.save()

                user_obj_2 = payment.objects.get(user = user_2)
                user_obj_2.amount += int(amount)
                user_obj_2.save()
                return Response({'Status':True, 'Msg':'Your payment has been successfully transfered'})
        except Exception as e:
            print(e)
            return Response('Something went wrong')