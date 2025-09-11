# controller/views.py
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Device
from .serializers import DeviceSerializer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def send_status_update(device_id, status, message):
    """A helper function to send a WebSocket update."""
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"device_{device_id}",
        {
            'type': 'send_device_status',
            'status': status,
            'message': message,
        }
    )

@api_view(['GET'])
def get_status(request, device_id):
    device, created = Device.objects.get_or_create(device_id=device_id)
    if not created:
        device.save()
        
    serializer = DeviceSerializer(device)
    return Response(serializer.data)

@api_view(['POST'])
def set_status(request, device_id):
    status = request.data.get('status')
    message = request.data.get('message', 'Device is locked by administrator.')

    if status not in ['active', 'locked']:
        return Response({"error": "Invalid status"}, status=400)

    device = get_object_or_404(Device, device_id=device_id)
    device.status = status
    
    if status == 'locked':
        device.lock_message = message
    else:
        device.lock_message = ""
    
    device.save()

    send_status_update(device.device_id, device.status, device.lock_message)
    return Response({"status": "updated", "device_id": device.device_id})
