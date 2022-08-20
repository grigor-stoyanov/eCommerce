from django.urls import path

from eCommerce.api.views.product_api_views import ProductListApiView,ProductUpdateApiView

urlpatterns = [
    path('products/', ProductListApiView.as_view(), name='get all products'),
    path('products/<int:pk>/', ProductUpdateApiView.as_view(), name='alter product')
]
