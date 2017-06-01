from rest_framework import serializers

from .models import Device


class DeviceSerializer(serializers.ModelSerializer):
    """Device Serializer"""

    class Meta:
        model = Device
        fields = ('__all__')
        read_only_fields = ('user', 'facility', )

