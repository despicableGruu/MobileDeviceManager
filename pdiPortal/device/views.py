"""
This is where the views for the device app are contained.
It has views to list device and get a selected device. It
also has an API for Device and Device Model CRUD.
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from profiles.models import PortalUser
from device.utils import get_device_list

from .utils import (
    get_device_list,
    check_device_model_exists,
)
from .models import Device
from .serializers import DeviceSerializer

# Create your views here.
@login_required
def devices(request):
    """ This returns all of the devices that the requesting user is permitted to see. """
    user = request.user
    device_list = get_device_list(user)
    context = {'user': user, 'device_list': device_list}
    template = 'devices/device_list.html'
    return render(request, template, context)

@method_decorator(login_required, name='dispatch')
class DevicesForUser(View):
    """ Class that returns the devices for a given user. """
    def get(self, request, username):
        """ This returns the devices associated with a specific user. """
        user = request.user
        requested_username = username
        if user.is_superuser:
            try:
                requested_user = PortalUser.objects.get(
                    username=requested_username
                ).get()
            except ObjectDoesNotExist:
                messages.error(request, "The user does not exist.")
                redirect('device_list')
            device_list = Device.objects.filter(
                user=requested_user
                ).order_by("androidId").order_by("heartbeat")
        elif user.is_facility_administrator:
            try:
                requested_user = PortalUser.objects.get(
                    username=requested_username,
                    facility=user.facility
                    ).get()
            except ObjectDoesNotExist:
                redirect('device_list')
            device_list = Device.objects.filter(
                user=requested_user,
                ).order_by("androidId").order_by("heartbeat")
        else:
            return redirect('dashboard')

        if requested_user.first_name:
            requested_username = requested_user.first_name

        context = {'user': user,
                   'device_list': device_list,
                   'requested_username': requested_username}
        template = 'devices/device_list_for_user.html'
        return render(request, template, context)

@login_required
def get_device(request):
    """ This is a view that will show the information for the specific device requested. """
    user = request.user
    requested_device = request.deviceId
    context = {
        'user': user,
        'device': requested_device
    }
    template = 'devices/device.html'
    return render(request, template, context)

class DeviceCreateReadView(ListCreateAPIView):
    """ This is part of the Device API where you can create new devices
    or return all of the devices. """
    def perform_create(self, serializer):
        check_device_model_exists(self.request.data['model'])
        device_instance = serializer.save(
            user=self.request.user,
            facility=self.request.user.facility
        )

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_field = 'android_id'


class DeviceReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """This is part of the API where you can Update, Read, or Delete a specific device."""

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_field = 'android_id'
