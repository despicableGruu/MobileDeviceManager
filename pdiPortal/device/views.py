import json

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.utils.decorators import method_decorator

from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from profiles.models import PortalUser

from .utils import get_device_list
from .models import Device
from .serializers import DeviceSerializer

# Create your views here.
@login_required
def devices(request):
    """ TODO: Docstring """
    user = request.user
    device_list = get_device_list(user)
    context = {'user': user, 'device_list': device_list}
    template = 'devices/device_list.html'
    return render(request, template, context)

@method_decorator(login_required, name='dispatch')
class DevicesForUser(View):
    """ TODO: Docstring """
    def get(self, request, username):
        """ TODO: Docstring """
        user = request.user
        requested_username = username
        if user.is_superuser:
            # if PortalUser.objects.filter(username=requested_username).count() == 0:
            #     return redirect('device-list')
            requested_user = PortalUser.objects.filter(username=requested_username)[0]
            device_list = Device.objects.filter(user=requested_user).order_by("androidId").order_by("heartbeat")
            if requested_user.first_name:
                requested_username = requested_user.first_name
        elif user.is_facility_administrator:
            if PortalUser.objects.filter(username=requested_username).count() == 0:
                return redirect('device-list')
            requested_user = PortalUser.objects.filter(username=requested_username)[0]
            facilities = user.facility.all()
            device_list = []
            for one_facility in facilities:
                device_objects = Device.objects.filter(facility=one_facility).order_by("androidId").order_by("heartbeat")
                for single_device in device_objects:
                    device_list.append(single_device)
            if requested_user.first_name:
                requested_username = requested_user.first_name
        else:
            return redirect('dashboard')
        context = {'user': user,
                   'device_list': device_list,
                   'requested_username': requested_username}
        template = 'devices/device_list_for_user.html'
        return render(request, template, context)

@login_required
def device(request):
    """ TODO: Docstring """
    user = request.user
    requested_device = request.deviceId
    context = {
        'user': user,
        'device': requested_device
    }
    template = 'devices/device.html'
    return render(request, template, context)

class DeviceCreateReadView(ListCreateAPIView):
    """ TODO: Docstring """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    lookup_field = 'android_id'


class DeviceReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    lookup_field = 'android_id'
