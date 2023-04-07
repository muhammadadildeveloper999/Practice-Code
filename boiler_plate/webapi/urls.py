from django.urls import path, include
from webapi.views import *

urlpatterns = [
    path('superadmin', crud.as_view()),
    path('login', login.as_view()),
    # path('signup', signup.as_view()), 
    path('getspaceficcategorydata', getspaceficcategorydata.as_view()),
    
]