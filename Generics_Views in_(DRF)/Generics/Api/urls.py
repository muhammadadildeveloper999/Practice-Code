from django.urls import path
from Api.views import *

urlpatterns = [
    path('genericsstudent', genericsstudent.as_view()),
    path('StudentGenerics/<pk>/',StudentGenerics.as_view()),

]