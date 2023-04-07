from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
# from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('api/', include('api.urls')),
    # path('Student_data/', views.Student_data),
    # path('Student_list/', views.Student_list),
]


