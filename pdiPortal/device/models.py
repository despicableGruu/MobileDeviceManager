from django.db import models
from facility.models import Facility
from profiles.models import PortalUser

# The default facility will always be PDi
DEFAULT_FACILITY_ID = 1

# Create your models here.
class DeviceModel(models.Model):
    """A class that holds all of the device models. This class is a useful reference
    for each defice, and for applications that may only work on certain devices"""
    device_model = models.CharField(max_length=40)

    def __str__(self):
        return self.device_model

class Device(models.Model):
    """A class that stores all of the data about a device in the database."""
    name = models.CharField(max_length=100, default='Android Device')
    android_id = models.CharField(max_length=25)
    build_number = models.CharField(max_length=25)
    operating_system_version = models.CharField(max_length=25)
    user = models.ForeignKey(PortalUser)
    facility = models.ForeignKey(Facility, default=DEFAULT_FACILITY_ID)
    model = models.ForeignKey(DeviceModel)
    heartbeat = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Operation(object):
    """A class for that stores the operations applied to a device."""

		