from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import facility, PortalUser

# Register your models here.
class facilityAdmin(admin.ModelAdmin):
    class Meta:
        model = facility

admin.site.register(facility, facilityAdmin)

admin.site.register(PortalUser)