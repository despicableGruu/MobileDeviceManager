from django.db import models
from django.utils import timezone
from device.models import Device, DeviceModel

# Create your models here.

def app_directory_path(instance, filename):
    """TODO: Docstring"""
    return 'upload/{0}/{1}/{2}'.format(instance.name, instance.version, filename)


def platform_path(instance, filename):
    """TODO: Docstring"""
    return 'upload/{0}/{1}'.format(instance.name, filename)

class Platform(models.Model):
    """TODO: Docstring"""
    name = models.CharField(max_length=25)
    icon = models.ImageField(upload_to=platform_path)

    def __str__(self):
        return self.name

class Application(models.Model):
    """Database table that stores all of the information
    for an application hosted on our store."""
    name = models.CharField(max_length=50)
    application_title = models.CharField(max_length=50)
    platform = models.ManyToManyField(
        Platform,
        through='AppPlatformList',
        through_fields=('app', 'platform'),
        )
    version = models.CharField(max_length=40)
    partNumber = models.CharField(max_length=15)
    pricePerMonth = models.FloatField()
    msrp = models.FloatField()
    description = models.TextField()
    recent_updates = models.TextField(blank=True)
    icon = models.ImageField(upload_to=app_directory_path)
    banner = models.ImageField(upload_to=app_directory_path)
    applicationFile = models.FileField(upload_to=app_directory_path)
    created = models.DateTimeField(auto_now_add=True)
    number_of_downloads = models.PositiveIntegerField(default=0)
    developer = models.CharField(max_length=100)
    valid_device_models = models.ManyToManyField(
        DeviceModel,
        through='AppModelList',
        through_fields=('app', 'device_model'),
        )

    def __str__(self):
        return self.name

class Screenshot(models.Model):
    """Table to hold all of the screenshots for
    the applications in our store."""

    screenshot_title = models.CharField(max_length=40, blank=True)
    application = models.ForeignKey(Application)
    image = models.ImageField(upload_to=app_directory_path)

class Video(models.Model):
    """TODO: Docstring"""
    video_title = models.CharField(max_length=40, blank=True)
    application = models.ForeignKey(Application)
    video = models.FileField(upload_to=app_directory_path)
    summary = models.TextField()

class Review(models.Model):
    """TODO: Docstring"""
    review_title = models.CharField(max_length=25, blank=True)
    body = models.TextField(max_length=1000, blank=True)
    rating = models.PositiveIntegerField()
    app = models.ForeignKey(Application)

    def __str__(self):
        return self.review_title

class DownloadedApp(models.Model):
    """A class that stores the downloaded applications to a device."""
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    downloadedDate = models.DateTimeField(auto_now_add=True)
    renewalDate = models.DateField(default=timezone.now)

    def __str__(self):
        return self.application.name

class AppModelList(models.Model):
    """TODO: Docstring"""
    app = models.ForeignKey(Application)
    device_model = models.ForeignKey(DeviceModel)

class AppPlatformList(models.Model):
    """TODO: Docstring"""
    app = models.ForeignKey(Application)
    platform = models.ForeignKey(Platform)
