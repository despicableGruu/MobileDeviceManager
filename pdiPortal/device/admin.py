from django.contrib import admin
from .models import DeviceModel, Device, DeviceFacilityList

# Register your models here.
admin.site.register(DeviceModel)
admin.site.register(Device)
admin.site.register(DeviceFacilityList)
