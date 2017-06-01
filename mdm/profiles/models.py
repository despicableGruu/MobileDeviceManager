from django.db import models
from django.contrib.auth.models import AbstractUser
from facility.models import Facility

# Create your models here.
class PortalUser(AbstractUser):
    """Custom user fields to be added to the default user"""
    facility = models.ForeignKey(Facility)
    is_facility_administrator = models.BooleanField(default=False)
    is_publisher = models.BooleanField(default=False)
    is_distributor = models.BooleanField(default=False)
