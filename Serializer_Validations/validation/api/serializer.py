from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
# from rest_framework.decorators import (api_view, permission_classes, list_route)
from django.http import Http404, HttpResponseForbidden
from django.contrib.auth import password_validation
import jwt
from django.contrib.auth.models import User
from .models import*
import re
from decouple import config

# class StudentSerialzer(serializers.Serializer):
#     name = serializers.CharField(max_length=100,default="" ) 
#     email = serializers.CharField(max_length=100,default="")
#     password = serializers.CharField(max_length=100,default="")
#     age = serializers.CharField(max_length=100,default="")
#     phone = serializers.CharField(max_length=100,default="")

class StudentSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Student
        fields = '__all__'
        fields = ['name', 'email', 'phone', 'password', 'age','rollno','address','mark']             

      # age validation
    
    def validate(self , data):
        if int(data['age' ]) < 18:
            raise serializers.ValidationError({'error' : "Age cannot be less than 18"})
   
        # email validation
    def validate_email(self, email):
        existing = Student.objects.filter(email=email).first()
        if existing:
            raise serializers.ValidationError("Someone with that email "
            "address has already registered. Was it you?")
        return email   


        # phone validation
    def validate_phone(self, phone):
        existing = Student.objects.filter(phone=phone).first()
        if existing:
            raise serializers.ValidationError("Someone with that phone "
            "number has already registered. Was it you?")
        return phone


        # password_validation
    def validate_password(self, value):
        password_validation.validate_password(value,self.instance)
        return value

        # numeric_name_validation
    def validate(self, data):
        if data['name']:
            for n in data['name']:   
                if n.isdigit():
                    raise serializers.ValidationError({'error' : "Name cannot be numeric"})
        
        return data     



# confirm_password validation
    # def validate(self, data):
    #     if not data.get('password') or not data.get('confirm_password'):
    #         raise serializers.ValidationError("Please enter a password and "
    #             "confirm it.")
    #     if data.get('password')  != data.get('confirm_password'):
    #         raise serializers.ValidationError("Those passwords don't match.")
        
    #     return data

   

#email user_name match validation
    # def validate(self, data):
    #     # Making sure the username always matches the email
    #     email = data.get('email', None)
    #     if email:
    #         data['name'] = email
    #     return data
    

    # password_validation
    # def validate_new_password(self, password):
    #     user = self.context['request'].user
    #     validate_password(password, user=user)

    #     username = user.username
    #     if len(username) and username.casefold() in password.casefold():
    #         raise serializers.ValidationError(
    #             _("The password is too similar to the username."))

    #     phone = user.phone
    #     if phone and phone_validator(phone):
    #         phone = str(parse_phone(phone).national_number)
    #         if phone in password:
    #             raise serializers.ValidationError(
    #                 _("Passwords cannot contain your phone."))

    #     return password 

