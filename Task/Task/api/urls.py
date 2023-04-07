from django.urls import path,include
from api.views import *

urlpatterns = [
    path( 'Stu_Class_Get', Stu_Class_Get.as_view()),
]