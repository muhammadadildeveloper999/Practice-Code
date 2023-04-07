from django.urls import path
from . import views

urlpatterns = [
    path('my_kafka_topic/', views.my_kafka_topic, name='my_kafka_topic'),
    # path('receive_message/', views.receive_message, name='receive_message'),
    # path('message_reciever/', views.message_reciever, name='message_reciever'),
    # path('send_message_to_kafka/', views.send_message_to_kafka, name='send_message_to_kafka'),

]
