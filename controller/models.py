# # controller/models.py
# from django.db import models
# from django.utils import timezone

# class Device(models.Model):
#     device_id = models.CharField(max_length=255, unique=True, help_text="The unique ANDROID_ID of the device.")
#     friendly_name = models.CharField(max_length=100, blank=True, help_text="e.g., Living Room TV, Office Display")
#     status = models.CharField(max_length=20, choices=[('active', 'Active'), ('locked', 'Locked')], default='active')
#     lock_message = models.TextField(blank=True, default="")
#     last_seen = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         if self.friendly_name:
#             return f"{self.friendly_name} ({self.device_id})"
#         return self.device_id

#     def save(self, *args, **kwargs):
#         self.last_seen = timezone.now()
#         super().save(*args, **kwargs)


from django.db import models
from django.utils import timezone

# --- Existing Device Model ---
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

# --- New AppVersion Model ---
class AppVersion(models.Model):
    version_code = models.IntegerField(unique=True, help_text="Must match the 'versionCode' in build.gradle")
    version_name = models.CharField(max_length=50, help_text="e.g. 1.0.2")
    download_url = models.URLField(help_text="Direct link to the APK file (e.g., GitHub Release asset)")
    release_notes = models.TextField(blank=True, help_text="What's new in this version?")
    is_mandatory = models.BooleanField(default=False, help_text="If true, user cannot skip this update")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-version_code'] # Ensures the latest version is always first in lists

    def __str__(self):
        return f"v{self.version_name} (Code: {self.version_code})"