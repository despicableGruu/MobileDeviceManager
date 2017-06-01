from django.db import models
from profiles.models import PortalUser

# Create your models here.
class Notification(models.Model):
    """Notifications for users"""
    title = models.CharField(max_length=25)
    body = models.TextField(max_length=500)
    action_url = models.URLField()
    user = models.ForeignKey(PortalUser)

    def __str__(self):
        return self.title
