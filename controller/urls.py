# controller/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('<str:device_id>/status/', views.get_status),  # GET request to get status
    path('<str:device_id>/status/set/', views.set_status),  # POST request to set status
]
