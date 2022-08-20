from rest_framework import generics as generic_api_views
from rest_framework.response import Response

from eCommerce.api.helpers.pagination import ProductPaginationStyle
from eCommerce.api.models import Product
from eCommerce.api.serializers.product_serializers import ProductSerializer


class ProductListApiView(generic_api_views.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPaginationStyle


class ProductUpdateApiView(generic_api_views.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
