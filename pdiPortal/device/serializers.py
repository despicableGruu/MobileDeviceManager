from rest_framework import serializers

from .models import Device

class DeviceSerializer(serializers.ModelSerializer):
    """Device Serializer"""
    class Meta:
        model = Device
        fields = ('name', 'android_id', 'build_number',
                  'operating_system_version')
