from django.urls import path,include
from file.views import *


urlpatterns = [
    path('UploadCsv_File', UploadCsv_File.as_view()),
    
    
]