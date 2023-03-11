from rest_framework import serializers

from ..models import Cart as CartModel
from ..serializers import CartItem as CartItemSerializer


class Cart(serializers.ModelSerializer):
    items = CartItemSerializer(source='cart', many=True)
    subtotal = serializers.SerializerMethodField()
    total_qty = serializers.SerializerMethodField()

    class Meta:
        model = CartModel
        fields = ('id', 'items', 'subtotal', 'total_qty')

    def get_subtotal(self, obj):
        subtotal = 0
        for cart_item in obj.cart.all():
            subtotal += cart_item.qty * cart_item.product.price
        return subtotal

    def get_total_qty(self, obj):
        total_qty = 0
        for cart_item in obj.cart.all():
            total_qty += cart_item.qty
        return total_qty
