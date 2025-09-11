# controller/models.py
from django.db import models
from django.utils import timezone

class Device(models.Model):
    device_id = models.CharField(max_length=255, unique=True, help_text="The unique ANDROID_ID of the device.")
    friendly_name = models.CharField(max_length=100, blank=True, help_text="e.g., Living Room TV, Office Display")
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('locked', 'Locked')], default='active')
    lock_message = models.TextField(blank=True, default="")
    last_seen = models.DateTimeField(default=timezone.now)

    def __str__(self):
        if self.friendly_name:
            return f"{self.friendly_name} ({self.device_id})"
        return self.device_id

    def save(self, *args, **kwargs):
        self.last_seen = timezone.now()
        super().save(*args, **kwargs)
