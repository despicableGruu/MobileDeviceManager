from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import facility, user

# Register your models here.
class facilityAdmin(admin.ModelAdmin):
    class Meta:
        model = facility

admin.site.register(facility, facilityAdmin)

class UserInline(admin.StackedInline):
    model = user
    can_delete = False
    verbose_name_plural = 'user'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)