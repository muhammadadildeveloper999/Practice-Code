from django.urls import path,include
from api.views import *


urlpatterns = [
    path('super', super.as_view()),
    # path('ExampleView', ExampleView.as_view())
    
    
]
