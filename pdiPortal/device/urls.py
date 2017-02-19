from django.conf.urls import url
from . import views as device_views

urlpatterns = [
    url(r'^device-list/$', device_views.devices, name='device-list'),
    url(
        r'^device-list/(?P<username>\w+)$',
        device_views.DevicesForUser.as_view(),
        name='device-list-for-user'
    ),
    url(r'^device/(?P<androidId>\w+)/$', device_views.device, name='device'),
    url(r'^api/$', device_views.DeviceCreateReadView.as_view(), name="device_rest_api"),
    url(
        r'^api/(?P<android_id>[-\w]+)/$',
        device_views.DeviceReadUpdateDeleteView.as_view(),
        name="device_rest_api"
    ),
]