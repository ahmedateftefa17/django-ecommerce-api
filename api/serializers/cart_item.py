from rest_framework import serializers

from ..models import CartItem as CartItemModel
from ..serializers.product import Product as ProductSerializer


class CartItem(serializers.ModelSerializer):
    product = ProductSerializer(many=False)
    subtotal = serializers.SerializerMethodField('get_subtotal')

    class Meta:
        model = CartItemModel
        fields = ('product', 'qty', 'subtotal')

    def get_subtotal(self, cart_item):
        return cart_item.qty * cart_item.product.price
