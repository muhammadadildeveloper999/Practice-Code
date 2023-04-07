from django.contrib import admin

# Register your models here.

from api.models import*

admin.site.register(Message)
admin.site.register(message_second)
