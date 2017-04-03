import json

from django.test import TestCase
from django.urls import reverse

from .serializers import DeviceSerializer
from .views import (
    DeviceCreateReadView,
    DeviceReadUpdateDeleteView,
    devices,
    get_device,
    DevicesForUser
)

def create_device(device_info):
    """This method will create a device from a dictionary."""
    device_info_json = json.JSONEncoder().encode(device_info)
    

