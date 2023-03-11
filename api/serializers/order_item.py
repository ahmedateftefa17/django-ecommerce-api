from rest_framework import serializers

from ..models import OrderItem as OrderItemModel
from ..serializers import Product as ProductSerializer


class OrderItem(serializers.ModelSerializer):
    product = ProductSerializer(many=False)
    subtotal = serializers.SerializerMethodField('get_subtotal')

    class Meta:
        model = OrderItemModel
        fields = ('product', 'qty', 'subtotal')

    def get_subtotal(self, order_item):
        return order_item.qty * order_item.product.price
