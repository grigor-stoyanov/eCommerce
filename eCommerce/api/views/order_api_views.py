from rest_framework import generics as generic_api_views
from eCommerce.api.helpers.pagination import GenericPaginationStyle
from eCommerce.api.models import Order

from eCommerce.api.serializiers import OrderSerializer


class OrderListApiView(generic_api_views.ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    pagination_class = GenericPaginationStyle


class OrderUpdateApiView(generic_api_views.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
