from django.urls import path

from eCommerce.api.views.order_api_views import OrderListApiView, OrderUpdateApiView
from eCommerce.api.views.product_api_views import ProductListApiView, ProductUpdateApiView

urlpatterns = [
    path('products/', ProductListApiView.as_view(), name='get all products'),
    path('products/<int:pk>/', ProductUpdateApiView.as_view(), name='alter product'),
    path('orders/', OrderListApiView.as_view(), name='get all orders'),
    path('orders/<int:pk>/', OrderUpdateApiView.as_view(), name='alter order')
]
