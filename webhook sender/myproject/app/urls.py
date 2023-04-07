from django.urls import path
from . import views
import os

urlpatterns = [
    path('webhook_sender/', views.webhook_sender, name='webhook_sender'),
    path('message_reciever/', views.message_reciever, name='message_reciever'),
    path('display_message/', views.display_message, name='display_message'),
    path('message_box/', views.message_box, name='message_box'),
    path('receiving_chats/', views.receiving_chats, name='receiving_chats'),
    
]