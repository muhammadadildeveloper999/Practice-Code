from rest_framework import serializers
from .models import*

# class UserVoteSerializer(serializers.ModelSerializer):
#     id = serializers.IntegerField(read_only=True)
#     created_by = serializers.CharField(read_only=True)

#     class Meta:
#         model = UserVote
#         fields = ('id', 'rating', 'created_by')
    

# class StudentSerialzer(serializers.Serializer):
#     name = serializers.CharField(max_length=100,default="" ) 
#     email = serializers.CharField(max_length=100,default="")
#     password = serializers.CharField(max_length=100,default="")
#     age = serializers.CharField(max_length=100,default="")
#     phone = serializers.CharField(max_length=100,default="")

# class Student(serializers.ModelSerializer):
    
#     class Meta:
#         model = Student
#         feilds = '__all__'

#     def validations(self , data):

#         if data['age' ] < 18:
#             raise serializers.ValidationError({"Age cannot be less than 18"})
             
#         return  data