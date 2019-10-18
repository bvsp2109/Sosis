from django.contrib import admin
from .models import *

# Register your models here

class FutureAdmin(admin.ModelAdmin):
    list_display = ['Name','Email','Aim','Date']
admin.site.register(Future,FutureAdmin)