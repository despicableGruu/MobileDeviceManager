from django.conf.urls import url
from . import views as device_views

urlpatterns = [
    url(r'^device-list/$', device_views.devices, name='device-list'),
    url(r'^device-list/(?P<username>\w+)$', device_views.DevicesForUser.as_view(), name='device-list-for-user'),
    url(r'^(?P<androidId>\w+)/$', device_views.device, name='device'),
    #url(r'^register/$', device_views.register_device.as_view(), name="register-device"),
]