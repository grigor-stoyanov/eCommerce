from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="Online Store API")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('eCommerce.api.urls')),
    path('docs/', schema_view),
]
