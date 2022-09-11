from rest_framework import serializers, fields
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


class ReportSerializer(serializers.Serializer):
    month = serializers.DateField()
    value = serializers.FloatField()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context['request'].query_params['metric'] == 'count':
            representation['value'] = int(representation['value'])
        return representation


class ValidateQueryParamsForReport(serializers.Serializer):
    date_start = fields.DateField(format='%Y%m%d')
    date_end = fields.DateField(format='%Y%m%d')
    metric = fields.ChoiceField(choices=['count', 'price'])
