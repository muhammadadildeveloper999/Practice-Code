from django.urls import path,include
from Api.views import *

urlpatterns = [
    path( 'Reservation_get', Reservation_get.as_view()),
]