from rest_framework import serializers

from device.models import Device
from profiles.models import PortalUser

from .models import Facility


class FacilitySerializer(serializers.ModelSerializer):
    """Facility serializer"""
    devices = serializers.PrimaryKeyRelatedField(many=True, queryset=Device.objects.all())
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=PortalUser.objects.all())

    class Meta:
        model = Facility
        fields = ('id', 'name', 'devices', 'users')

        