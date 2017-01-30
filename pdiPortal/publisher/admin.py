from django.contrib import admin
from .models import Application, Platform

# Register your models here.
admin.site.register(Application)
admin.site.register(Platform)