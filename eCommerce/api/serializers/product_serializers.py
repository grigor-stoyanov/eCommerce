from rest_framework import serializers

from eCommerce.api.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pk', 'title', 'price')
