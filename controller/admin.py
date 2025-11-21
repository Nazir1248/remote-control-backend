# # controller/admin.py
# from django.contrib import admin
# from .models import Device
# from .views import send_status_update

# @admin.register(Device)
# class DeviceAdmin(admin.ModelAdmin):
#     list_display = ('__str__', 'status', 'last_seen')
#     list_editable = ('status',)
#     search_fields = ('device_id', 'friendly_name')
#     list_filter = ('status',)
#     fieldsets = (
#         (None, {'fields': ('device_id', 'friendly_name')}),
#         ('Control', {'fields': ('status', 'lock_message')}),
#         ('Metadata', {'fields': ('last_seen',)}),
#     )
#     readonly_fields = ('device_id', 'last_seen')

#     def save_model(self, request, obj, form, change):
#         """
#         This version includes print statements for debugging.
#         """
#         # --- Start of Debugging ---
#         print("\n" + "="*50)
#         print("--- DEBUG: Inside save_model function ---")
#         print(f"--- 1. State BEFORE logic: status='{obj.status}', message='{obj.lock_message}' ---")
#         # --- End of Debugging ---

#         message_to_send = obj.lock_message
        
#         if obj.status == 'active':
#             obj.lock_message = ""
#             message_to_send = ""
#             print("--- 2. Logic path taken: Status is 'active'. Clearing message. ---")
#         elif not obj.lock_message:
#             default_message = "This device is locked by an administrator."
#             obj.lock_message = default_message
#             message_to_send = default_message
#             print("--- 2. Logic path taken: Status is 'locked' and message was EMPTY. Setting default message. ---")
#         else:
#             print("--- 2. Logic path taken: Status is 'locked' and message already had content. ---")

#         # --- Start of Debugging ---
#         print(f"--- 3. State AFTER logic (before saving): status='{obj.status}', message='{obj.lock_message}' ---")
#         # --- End of Debugging ---
        
#         super().save_model(request, obj, form, change)
        
#         # --- Start of Debugging ---
#         print("--- 4. Model has been saved to the database. ---")
#         print(f"--- 5. Sending WebSocket update with message: '{message_to_send}' ---")
#         print("="*50 + "\n")
#         # --- End of Debugging ---
        
#         send_status_update(obj.device_id, obj.status, message_to_send)


from django.contrib import admin
from .models import Device, AppVersion  # Added AppVersion here
from .views import send_status_update

# --- Existing Device Admin ---
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status', 'last_seen')
    list_editable = ('status',)
    search_fields = ('device_id', 'friendly_name')
    list_filter = ('status',)
    fieldsets = (
        (None, {'fields': ('device_id', 'friendly_name')}),
        ('Control', {'fields': ('status', 'lock_message')}),
        ('Metadata', {'fields': ('last_seen',)}),
    )
    readonly_fields = ('device_id', 'last_seen')

    def save_model(self, request, obj, form, change):
        """
        This version includes print statements for debugging.
        """
        # --- Start of Debugging ---
        print("\n" + "="*50)
        print("--- DEBUG: Inside save_model function ---")
        print(f"--- 1. State BEFORE logic: status='{obj.status}', message='{obj.lock_message}' ---")
        # --- End of Debugging ---

        message_to_send = obj.lock_message
        
        if obj.status == 'active':
            obj.lock_message = ""
            message_to_send = ""
            print("--- 2. Logic path taken: Status is 'active'. Clearing message. ---")
        elif not obj.lock_message:
            default_message = "This device is locked by an administrator."
            obj.lock_message = default_message
            message_to_send = default_message
            print("--- 2. Logic path taken: Status is 'locked' and message was EMPTY. Setting default message. ---")
        else:
            print("--- 2. Logic path taken: Status is 'locked' and message already had content. ---")

        # --- Start of Debugging ---
        print(f"--- 3. State AFTER logic (before saving): status='{obj.status}', message='{obj.lock_message}' ---")
        # --- End of Debugging ---
        
        super().save_model(request, obj, form, change)
        
        # --- Start of Debugging ---
        print("--- 4. Model has been saved to the database. ---")
        print(f"--- 5. Sending WebSocket update with message: '{message_to_send}' ---")
        print("="*50 + "\n")
        # --- End of Debugging ---
        
        send_status_update(obj.device_id, obj.status, message_to_send)

# --- New AppVersion Admin ---
@admin.register(AppVersion)
class AppVersionAdmin(admin.ModelAdmin):
    list_display = ('version_code', 'version_name', 'created_at', 'is_mandatory')
    ordering = ('-version_code',)