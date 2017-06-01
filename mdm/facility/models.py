from django.db import models

# Create your models here.
class Facility(models.Model):
    """Facility information for each installation"""
    name = models.CharField(max_length=150, unique=True)
    shippingAddress = models.CharField(max_length=200)
    billingAddress = models.CharField(max_length=200)

    def __str__(self):
        return self.name


