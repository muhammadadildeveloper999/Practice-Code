from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from webapi.models import*
from passlib.hash import django_pbkdf2_sha256 as handler
from django.db.models import Q
import webapi.usable as uc
from decouple import config
import jwt
# # Create your views here.

class crud(APIView):
    # Get Api
    def get(self, resquest):
        data = Super_AdminAcount.objects.values('Fname', 'Lname', 'Email', 'Username', 'Password', 'ContactNo', 'Role', 'Profile')

        return Response({'status':True, 'data':data})

        
        # PAPIViewost Api
    def post(self,request):
        fname = request.data['Fname']
        lname = request.data['Lname']
        email = request.data['Email']
        username = request.data['Username']
        password = handler.hash(request.data['Password'])
        contact = request.data['ContactNo']
        role = request.data['Role']

      
        data = Super_AdminAcount(Fname = fname,Lname = lname,Email = email,Username = username,Password = password,ContactNo =contact,Role = role,Profile = profile)

        data.save()

        return Response({'status':True, 'msg':'added successfully'})


#   Put Api
    def put(self,request):
        Id = request.data['Id']
        Fname = request.data['Fname']
        Lname = request.data['Lname']
        Email = request.data['Email']
        Username = request.data['Username']
        
        checkSuper_AdminAcount = Super_AdminAcount.objects.filter(Id=Id).first() 
        if checkSuper_AdminAcount:    
            checkSuper_AdminAcount.Fname=Fname
            checkSuper_AdminAcount.Lname=Lname
            checkSuper_AdminAcount.Email=Email
            checkSuper_AdminAcount.Username=Username
            checkSuper_AdminAcount.save()
            return Response({'status':True, 'msg':'Update successfully'})

        else:
            return Response({'status':True, 'msg':'Data not found'})

    # # Delete Api
    def delete (self,request):
        Id = request.GET['Id']
        data = Super_AdminAcount.objects.filter(Id=Id).first() 
            
        if data:
            data.delete()

            return Response({'status':True, 'msg':'delete successfully'})
 
        else:
            return Response({'status':False, 'msg':'Data is not found'})


# login Api

class login(APIView):
    def post(self,request):
        
           
        Email = request.data['Email']
        Password = request.data['Password']

        fetchuser = Super_AdminAcount.objects.filter(Email = Email).first()
        if fetchuser and handler.verify(Password,fetchuser.Password):
            # if not fetchuser.status == "Disable":
                access_token_payload = {
                
                    "Id":fetchuser.Id,
                    "Fname":fetchuser.Fname,
                    "Lname":fetchuser.Lname,
                    "Role":fetchuser.Role,
                    "Email":fetchuser.Email, 
                    "ContactNo":fetchuser.ContactNo,
                }
                
                access_token = jwt.encode(access_token_payload,config('superadminjwttoken'), algorithm='HS256')
    
              
                
                return Response({"status":True,"message":"Login Successfully","token":access_token},200)

        else:
            return Response({'status':False,'message':'Invalid Credential'},status = 401)

class signup(APIView):
    def post(self,request):

        Fname = request.data['Fname']
        Username = request.data['Username']
        ContactNo = request.data['ContactNo']
        Password = request.data['Password']
        Email = request.data['Email']


        # emailchecker = uc.checkemailforamt(Email)  
        # if not emailchecker:
        #     return Response({'status':False, 'msg': 'incorrect email format'})
        # passwordchecker = uc.PasswordLenghtValidator(Password)
        # if not passwordchecker:
        #     return Response({'status':False, 'msg': 'Password should not be greater than 8 or less than 20'})


        data = Super_AdminAcount(Fname = Fname, Username = Username, Password=handler.hash(Password), Email = Email, ContactNo= ContactNo)

        data.save()

        return Response({'status':True, 'msg':'SignUp successfully'})        


# practice_signup_api

class signup (APIView):
    def post (self, request):
        Fname = request.data['Fname']
        Username = request.data['Username']
        ContactNo = request.data['ContactNo']
        Password = request.data['Password']
        Email = request.data['Email']
         


        emailchecker = uc.checkemailforamt(Email)  
        if not emailchecker:
            return Response({'status':False, 'msg': 'incorrect email format'})
        passwordchecker = uc.PasswordLenghtValidator(Password)
        if not passwordchecker:
            return Response({'status':False, 'msg': 'Password should not be greater than 8 or less than 20'})
        
       
        data = Super_AdminAcount(Fname = Fname, Username = Username, Password=handler.hash(Password), Email = Email, ContactNo= ContactNo)

        data.save()

        return Response({'status':True, 'msg':'SignUp successfully'})        


class getspaceficcategorydata(APIView):
    def get (self, request):
        Id = request.GET['Id']
        # Fname = request.data['Fname']
        # Lname = request.data['Lname']
        # Email = request.data['Email']
        # Username = request.data['Username']
        # Password = handler.hash(request.data['Password'])
        # ContactNo = request.data['ContactNo']
        # Role = request.data['Role']
        # Profile = request.data['Profile']
        
        data = Super_AdminAcount.objects.filter(Id =Id).values('Id','Lname','Fname','Username','Password','ContactNo','Role','Profile').first()


        if data:
            return Response({'status':True, 'data':data})        
       
        else:
            return Response({'status':True, 'msg':'data not Found'})        
    



