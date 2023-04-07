from django.urls import path,include
from Api.views import *


urlpatterns = [
    # path('employees', employees.as_view()),
    path('search_field', search_field.as_view()),

]
