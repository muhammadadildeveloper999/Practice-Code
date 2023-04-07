from django.urls import path,include
from middle.views import *


urlpatterns = [
    path('signup', signup.as_view()),
    path('login', login.as_view()),
    path('ExampleView', ExampleView.as_view()),
    
    
]