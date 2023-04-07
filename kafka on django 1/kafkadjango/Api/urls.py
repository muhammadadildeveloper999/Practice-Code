from django.urls import path,include
from . import views
from Api.views import *

urlpatterns = [
# path('login/', views.login, name='login'),
path('send_message_to_kafka/', views.send_message_to_kafka, name='send_message_to_kafka'),
path('signup',signup.as_view()),
# path('send_message/', views.send_message_to_kafka, name='send_message'),

]