from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Entertainments API",
        default_version='v1',
        description="API for Entertainments",
        terms_of_service="http://www.it-shag.com/terms/",
        contact=openapi.Contact(email="contact@gmail.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('entertainments.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=8), name='schema-swagger-ui'),
]
