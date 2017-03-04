from rest_framework import serializers

from .models import Device, DeviceModel

class DeviceSerializer(serializers.ModelSerializer):
    """Device Serializer"""
    user = serializers.ReadOnlyField(source='user')
    device_model = serializers.ReadOnlyField(source="device_model")
    facility = serializers.ReadOnlyField(source="facility")

    class Meta:
        model = Device
        fields = ('name', 'android_id', 'build_number',
                  'operating_system_version', 'user', 'device_model', 'facility')


class DeviceModelSerializer(serializers.ModelSerializer):
    """Device Model serializer"""
    devices = serializers.PrimaryKeyRelatedField(many=True, queryset=Device.objects.all())

    class Meta:
        model = DeviceModel
        fields = ('id', 'device_model', 'devices')

