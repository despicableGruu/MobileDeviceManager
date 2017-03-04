from rest_framework import serializers

from device.models import Device

from .models import PortalUser

class ProfileSerializer(serializers.ModelSerializer):
    """Profile serializer"""
    devices = serializers.PrimaryKeyRelatedField(many=True, queryset=Device.objects.all())

    class Meta:
        model = PortalUser
        fields = ('id', 'username', 'devices')

