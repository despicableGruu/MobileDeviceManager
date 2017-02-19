from django.conf.urls import url
from . import views as store_views

urlpatterns = [
    url(r'^apps/$', store_views.app_list, name='applications'),
    url(r'^app/(?P<name>\w+)/$', store_views.app_page, name='appPage'),
]