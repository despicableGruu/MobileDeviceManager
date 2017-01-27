"""pdiPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from management import views as management_views
from store import views as store_views
from device import views as device_views
from profiles import views as profile_views
from contact import views as contact_views
from publisher import views as publisher_views
from facility import views as facility_views

urlpatterns = [
	url(r'^$', store_views.store, name='home'),
    url(r'^contact/$', contact_views.contact, name='contact'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/password/change/$', management_views.dashboard_after_password_change, name='account_change_password'),
	url(r'^accounts/', include('allauth.urls')),
    #url(r'^review/', include('review.urls')),
	url(r'^dashboard/$', management_views.dashboard, name='dashboard'),
    url(r'^device-list/$', device_views.devices, name='device-list'),
    url(r'^device-list/(?P<username>\w+)$', device_views.devices_for_user.as_view(), name='device-list-for-user'),
    url(r'^device/(?P<androidId>\w+)/$', device_views.device, name='device'),
    url(r'^register/device/$', device_views.register_device.as_view(), name="register-device"),
    url(r'^users/$', profile_views.users.as_view(), name='users'),
    url(r'^users/(?P<username>\w+)/$', profile_views.user_configuration, name="user-configuration"),
    url(r'^create/facilityadmin/$', profile_views.create_facility_admin.as_view(), name='create-admin'),
    url(r'^create/user/$', profile_views.create_user.as_view(), name='create-user'),
    url(r'^reports/$', management_views.reports, name='reports'),
    url(r'^store/$', store_views.store, name='store'),
    url(r'^store/apps/$', store_views.app_list, name='applications'),
    url(r'^store/app/(?P<name>\w+)/$', store_views.app_page, name='appPage'),
    url(r'^publisher/$', publisher_views.publisher, name='publisher'),
    url(r'^publisher/createApp/$', publisher_views.create_application, name="create-app")
]
