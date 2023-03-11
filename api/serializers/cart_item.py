from rest_framework import serializers

from ..models import CartItemModel
from ..serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(many=False)
    subtotal = serializers.SerializerMethodField('get_subtotal')

    class Meta:
        model = CartItemModel
        fields = ('product', 'qty', 'subtotal')

    def get_subtotal(self, cart_item):
        return cart_item.qty * cart_item.product.price
