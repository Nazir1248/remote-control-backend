# controller/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class DeviceStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.device_id = self.scope['url_route']['kwargs']['device_id']
        self.room_group_name = f"device_{self.device_id}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        pass

    async def send_device_status(self, event):
        """
        This method is called when a message is sent to this consumer's group.
        It constructs a JSON payload with the device status and message.
        """
        status_data = {
            'status': event['status'],
            'message': event.get('message', 'Device is locked.'),
            # 'qr_url' is no longer part of the event
        }
        
        await self.send(text_data=json.dumps(status_data))
