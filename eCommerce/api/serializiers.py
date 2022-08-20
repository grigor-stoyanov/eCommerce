from rest_framework import serializers
from eCommerce.api.models import Order
from eCommerce.api.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('pk', 'title', 'price')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(OrderSerializer, self).to_representation(instance)
        representation['products'] = ProductSerializer(instance.products.all(), many=True).data
        return representation