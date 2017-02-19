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
from contact import views as contact_views
from reports import views as report_views

urlpatterns = [
    url(r'^$', store_views.store, name='home'),
    url(r'^contact/$', contact_views.contact, name='contact'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/password/change/$', management_views.CustomPasswordChange.as_view(), name='account_change_password'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^devices/', include('device.urls')),
    url(r'^users/', include('profiles.urls')),
    url(r'^store/', include('store.urls')),
    #url(r'^review/', include('review.urls')),
    url(r'^dashboard/$', management_views.dashboard, name='dashboard'),
    url(r'^reports/$', report_views.reports, name='reports'),
    url(r'^publisher/', include('publisher.urls')),
]
