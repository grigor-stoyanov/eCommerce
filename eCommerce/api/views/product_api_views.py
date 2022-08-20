from rest_framework import generics as generic_api_views
from eCommerce.api.helpers.pagination import GenericPaginationStyle
from eCommerce.api.models import Product
from eCommerce.api.serializiers import ProductSerializer


class ProductListApiView(generic_api_views.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = GenericPaginationStyle


class ProductUpdateApiView(generic_api_views.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
