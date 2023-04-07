from django.contrib import admin

from core.models import *


class FileAdmin(admin.ModelAdmin):

    list_display = ["id", "staff_name", "position", "age",   "year_joined"]

admin.site.register(File, FileAdmin)
