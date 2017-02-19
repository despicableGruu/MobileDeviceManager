from django.conf.urls import url
from . import views as profile_views

urlpatterns = [
    url(r'^$', profile_views.Users.as_view(), name='users'),
    url(r'^(?P<username>\w+)/$', profile_views.user_configuration, name="user-configuration"),
    url(r'^create/facilityadmin/$', profile_views.CreateFacilityAdmin.as_view(), name='create-admin'),
    url(r'^create/user/$', profile_views.CreateUser.as_view(), name='create-user'),
]