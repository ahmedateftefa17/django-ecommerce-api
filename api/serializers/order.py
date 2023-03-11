from rest_framework import serializers

from ..models import OrderModel
from ..serializers import OrderItemSerializer


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(source='order', many=True)
    subtotal = serializers.SerializerMethodField()
    total_qty = serializers.SerializerMethodField()

    class Meta:
        model = OrderModel
        fields = ('id', 'items', 'subtotal', 'total_qty')

    def get_subtotal(self, obj):
        subtotal = 0
        for order_item in obj.order.all():
            subtotal += order_item.qty * order_item.product.price
        return subtotal

    def get_total_qty(self, obj):
        total_qty = 0
        for order_item in obj.order.all():
            total_qty += order_item.qty
        return total_qty
