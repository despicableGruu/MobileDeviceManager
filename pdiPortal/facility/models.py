from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class facility(models.Model):
	"""Facility information for each PDi installation"""
	name = models.CharField(max_length=150, unique=True)
	shippingAddress = models.CharField(max_length=200)
	billingAddress = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class user(models.Model):
	"""Custom user fields to be added to the default user"""
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	facility = models.ForeignKey(facility)
	is_facility_administrator = models.BooleanField(default=False)
	is_publisher = models.BooleanField(default=False)



class notification(models.Model):
	"""Notifications for users"""
	title = models.CharField(max_length=25)
	body = models.TextField(max_length=500)
	action_url = models.URLField()
	user = models.ForeignKey(user)

	def __str__():
		return self.title
