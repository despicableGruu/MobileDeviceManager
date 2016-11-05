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
from contact import views as contact_views
from publisher import views as publisher_views
from facility import views as facility_views

urlpatterns = [
	url(r'^$', store_views.store, name='home'),
    url(r'^contact/$', contact_views.contact, name='contact'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/password/change/$', management_views.dashboard_after_password_change, name='account_change_password'),
	url(r'^accounts/', include('allauth.urls')),
    url(r'^review/', include('review.urls')),
	url(r'^dashboard/$', management_views.dashboard, name='dashboard'),
    url(r'^device-list/$', management_views.devices, name='device-list'),
    url(r'^device/(?P<androidId>\w+)/$', device_views.device, name='device'),
    url(r'^register/device/$', device_views.register_device, name="register-device"),
    url(r'^users/$', management_views.users, name='users'),
    url(r'^create/facilityadmin/$', facility_views.create_facility_admin, name='create-admin'),
    url(r'^reports/$', management_views.reports, name='reports'),
    url(r'^store/$', store_views.store, name='store'),
    url(r'^store/app/(?P<name>\w+)/$', store_views.appPage, name='appPage'),
    url(r'^publisher/$', publisher_views.publisher, name='publisher'),
]
