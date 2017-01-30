from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Facility

# Register your models here.
class FacilityAdmin(admin.ModelAdmin):
    """ TODO: Docstring """
    class Meta:
        model = Facility

admin.site.register(Facility, FacilityAdmin)
