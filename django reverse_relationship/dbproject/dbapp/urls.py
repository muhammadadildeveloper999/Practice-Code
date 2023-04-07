from django.urls import path,include
from dbapp.views import *


urlpatterns = [
    path('resverse_relationship', resverse_relationship.as_view()),
    # path('login', login.as_view()),

]