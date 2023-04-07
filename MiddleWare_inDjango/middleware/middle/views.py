from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from django.shortcuts import render
from django.db.models import Q
from passlib.hash import django_pbkdf2_sha256 as handler
from middle.models import *
import middle.usable as uc
from decouple import config
from django.http import HttpResponse
import jwt
import datetime

# signup

class signup(APIView):
    def post(self,request):                                                                                                                         
        firstname =request.data.get("firstname")
        lastname = request.data.get("lastname")
        address = request.data.get("address")
        password=request.data.get('password')
        email=request.data.get('email')
        phone=request.data.get('phone')                                                               

        if uc.checkemailforamt(email):
            if not uc.passwordLengthValidator(password):
                return Response({"status":False, "message":"Password should not be than 8 or greater than 20"})

            checkemail=account.objects.filter(email=email).first()
            if checkemail:
                return Response({"status":False, "message":"Email already exists"})
  
            checkphone=account.objects.filter(phone=phone).first()
            if checkphone:
                return Response({"status":False, "message":"phone no already existsplease try different number"})
        
            data = account(firstname=firstname,lastname=lastname,password= handler.hash(password),email = email, 
            phone=phone, address=address)
            data.save()

            return Response({"status":True,"message":"Account Created Successfully"},201)
 
        else:
            return Response({"status":False,"message":"Email Format Is Incorrect"},422)
 
 ################################################################################################################################################
# login admin&company
class login(APIView):
    def post (self,request):

        email = request.data.get('email')
        password = request.data.get('password')

        fetchAccount = account.objects.filter(email=email).first() 
        if fetchAccount:
            if handler.verify(password,fetchAccount.password):
                if fetchAccount.role == "admin":
                    access_token_payload = {
                                    'id': fetchAccount.id,
                                    'email':fetchAccount.email,
                                    'firstname':fetchAccount.firstname,
                                    'exp':datetime.datetime.utcnow() + datetime.timedelta(days=22),
                                    'iat':datetime.datetime.utcnow(),}

                    access_token = jwt.encode(access_token_payload,config('adminkey'),algorithm = 'HS256')
                    data = {'firstname':fetchAccount.firstname, 'lastname':fetchAccount.lastname, 'email':fetchAccount.email, 'phone':fetchAccount.phone,
                    'address':fetchAccount.address}
                    
                    return Response({"status":True,"message":"Login Successlly","token":access_token,"admindata":data},200)

            
                else: 
                    access_token_payload = {
                                'id': fetchAccount.id,
                                'firstname':fetchAccount.firstname, 
                                'email':fetchAccount.email, 
                                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=22),
                                'iat': datetime.datetime.utcnow(),

                            }

                    access_token = jwt.encode(access_token_payload,config('companykey'),algorithm = 'HS256')
                    data = {'firstname':fetchAccount.firstname, 'lastname':fetchAccount.lastname, 'email':fetchAccount.email, 'phone':fetchAccount.phone,
                    'address':fetchAccount.address}                
                    return Response({"status":True,"message":"Login Successlly","token":access_token,"companydata":data},200)

            else:
                return Response({"status":False,"message":"Invalid credientials"},200)

# ExamplesView

class ExampleView(APIView):
    permissions_clases=['admin','adminkey']
    def post(self, request):
        requireFields = ['firstname','lastname','address','email','password','phone']
        validator = uc.keyValidation(True,True,request.data,requireFields)
        
        if validator:
            return Response(validator,status = 200)   
                                                                      
        else:                                                
            firstname = request.data.get("firstname")
            lastname = request.data.get("lastname")
            address = request.data.get("address")
            email=request.data.get("email")
            password=request.data.get("password")
            phone=request.data.get("phone")

            data = account(firstname=firstname,lastname=lastname,address=address,email=email,password=password,phone=phone)
            data.save()

            return Response({"status":True,"message":"Successfully Post"},201)
    
########################################################################################################################################################
    def get(self, request):
    
        data = account.objects.all().values('firstname','lastname','email','address','password','phone')
        
        return Response({'status':True, 'data': data}) 
        
######################################################################################################################################################################################################################33
    
    def put(self, request):
        requireFields = ['firstname','lastname','address','email','password','phone']
        validator = uc.keyValidation(True,True,request.data,requireFields)


        if validator:
            return Response(validator,status = 200)   

        else:       
            id = request.data.get('id')   
            firstname = request.data.get("firstname")
            lastname = request.data.get("lastname")
            address = request.data.get("address")
            email= request.data.get("email")     
            password= request.data.get("password")      
            phone= request.data.get("phone")      

            admin = account.objects.filter(id=id).first()
            if admin:
                admin.firstname=firstname
                admin.lastname=lastname
                admin.address=address
                admin.email=email
                admin.password=password
                admin.phone=phone

                admin.save()

                return Response({'status': True, 'Msg': 'data Update Successfully'}) 

            else:
                return Response({"status": False, "msg":"Unauthorized"})
        
####################################################################################################################################################
    
    def delete(self,request):
        requireField = ['id']
        validator = uc.keyValidation(True,True,request.GET,requireField)

    
        if validator:
            return Response(validator,status = 200)   

        else:
            id = request.GET['id']
    
        data = account.objects.filter(id=id).first()       
        if data:
            data.delete()
            return Response({'status': True, 'Msg': 'data Delete Successfully'}) 
        else:
            return Response({"status": False, "msg":"Unauthorized"})

# ==================================================================================================================================================
