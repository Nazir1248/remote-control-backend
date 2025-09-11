# """
# URL configuration for remotecontrol project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# # remotecontrol/urls.py
# from django.contrib import admin
# from django.urls import path, include, re_path
# from rest_framework import permissions
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi

# # --- Swagger UI Configuration ---
# schema_view = get_schema_view(
#    openapi.Info(
#       title="Remote Control API",
#       default_version='v1',
#       description="API for remotely controlling Android devices.",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@example.com"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('controller.urls')),
#     re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]



# remotecontrol/urls.py
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# --- Swagger UI Configuration ---
schema_view = get_schema_view(
   openapi.Info(
      title="Remote Control API",
      default_version='v1',
      description="API for remotely controlling Android devices.",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# --- Main URL List ---
urlpatterns = [
    # Path for the Admin Dashboard (now styled by Jazzmin)
    path('admin/', admin.site.urls),

    # Path for your API
    path('api/', include('controller.urls')),

    # Paths for the Swagger API Documentation UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]