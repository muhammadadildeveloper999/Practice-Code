from django.urls import path,include
from Api.views import *

urlpatterns = [

# ADMIN-SITE-URLS

path('Home',Home.as_view()),
]