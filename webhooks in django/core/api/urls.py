from django.urls import path
from . import views

urlpatterns = [
    path('webhook_send_message/', views.webhook_send_message, name='webhook_send_message'),
    path('send_message/', views.send_message, name='send_message'),
    path('receive_notification/', views.receive_notification, name='receive_notification'),
    path('reciever/', views.reciever, name='reciever'),
    path('messager_recieving/', views.messager_recieving, name='messager_recieving'),
    path('receive_notificationother/', views.receive_notificationother, name='receive_notificationother'),

]
