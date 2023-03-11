from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from ..models import Cart as CartModel, CartItem as CartItemModel, Product as ProductModel
from ..serializers import CartItem as CartItemSerializer, Cart as CartSerializer


class CartItems(generics.ListCreateAPIView):
    def create(self, request):
        product_id = request.data['product']

        try:
            product = ProductModel.objects.filter(pk=product_id).get()
        except:
            return Response({
                'product': 'Product does not exist!',
            }, status=status.HTTP_400_BAD_REQUEST)

        user = request.user

        try:
            cart = CartModel.objects.filter(user=user.id).get()
        except:
            cart = CartModel.objects.create(user=user)

        try:
            cart_item = CartItemModel.objects.filter(
                cart=cart.id, product=product.id).get()
            cart_item.qty += 1
            cart_item.save()
        except:
            cart_item = CartItemModel.objects.create(
                cart=cart, product=product, qty=1)

        return Response(CartSerializer(cart, many=False).data)

    def list(self, request):
        user = request.user

        subtotal = 0
        total_qty = 0

        try:
            cart = CartModel.objects.filter(user=user.id).get()
        except:
            return Response({
                'items': [],
                'subtotal': subtotal,
                'total_qty': total_qty,
            })

        return Response(CartSerializer(cart, many=False).data)


cart_items_view = CartItems.as_view()
