from django.db import models
from datetime import date
from django.utils import timezone
from django.contrib.auth.models import User
from facility.models import facility

DEFAULT_FACILITY_ID = 1

# Create your models here.
class DeviceModel(models.Model):
	"""docstring for Model"""	
	device_model = models.CharField(max_length=40)

	def __str__(self):
		return self.device_model

class Device(models.Model):
	"""docstring for Device"""
	name = models.CharField(max_length=100, default='Android Device')
	androidId = models.CharField(max_length=25)
	buildNumber = models.CharField(max_length=25)
	osVersion = models.CharField(max_length=25)
	user = models.ForeignKey(User)
	facility = models.ForeignKey(facility, default = DEFAULT_FACILITY_ID)
	device_model = models.ForeignKey(DeviceModel)
	heartbeat = models.BooleanField(default=False)

	def __str__(self):
		return self.name

class downloadedApp(models.Model):
	application = models.ForeignKey('application.Application', on_delete=models.CASCADE)
	device = models.ForeignKey(Device, on_delete=models.CASCADE)
	downloadedDate=models.DateTimeField(auto_now_add=True)
	renewalDate = models.DateField(default=timezone.now)


	def __str__(self):
		return self.name

		
class operation(object):
	"""docstring for operation"""
	
		