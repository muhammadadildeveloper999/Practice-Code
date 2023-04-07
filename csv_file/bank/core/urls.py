from django.urls import path

from core.views import *

urlpatterns = [

    path('upload/', upload_file.as_view(), name='upload-file')
]