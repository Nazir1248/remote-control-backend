# controller/serializers.py
from rest_framework import serializers
from .models import Device

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        # THE FIX: Add 'lock_message' to this list. This ensures the
        # Android app receives the message when it first starts up.
        fields = ['device_id', 'status', 'lock_message']
