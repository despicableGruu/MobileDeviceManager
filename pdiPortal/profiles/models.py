from django.db import models
from django.contrib.auth.models import AbstractUser
from facility.models import facility

# Create your models here.
class PortalUser(AbstractUser):
  """Custom user fields to be added to the default user"""
  facility = models.ManyToManyField(facility)
  is_facility_administrator = models.BooleanField(default=False)
  is_publisher = models.BooleanField(default=False)
  is_distributor = models.BooleanField(default=False)



class notification(models.Model):
  """Notifications for users"""
  title = models.CharField(max_length=25)
  body = models.TextField(max_length=500)
  action_url = models.URLField()
  user = models.ForeignKey(PortalUser)

  def __str__():
    return self.title