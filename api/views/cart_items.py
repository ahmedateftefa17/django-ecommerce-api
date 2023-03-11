from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from ..models import Cart as CartModel, CartItem as CartItemModel, Product as ProductModel
from ..serializers.cart_item import CartItem as CartItemSerializer


class CartItems(generics.ListCreateAPIView):
    queryset = CartItemModel.objects.all()
    serializer_class = CartItemSerializer

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

        cart_items = CartItemModel.objects.filter(cart=cart.id).all()
        cart_items_serializer = CartItemSerializer(cart_items, many=True)

        subtotal = 0
        total_qty = 0
        for cart_item in cart_items:
            subtotal += cart_item.qty * cart_item.product.price
            total_qty += cart_item.qty

        return Response({
            'items': cart_items_serializer.data,
            'subtotal': subtotal,
            'total_qty': total_qty,
        })

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

        cart_items = CartItemModel.objects.filter(cart=cart.id).all()
        cart_items_serializer = CartItemSerializer(cart_items, many=True)
        for cart_item in cart_items:
            subtotal += cart_item.qty * cart_item.product.price
            total_qty += cart_item.qty

        return Response({
            'items': cart_items_serializer.data,
            'subtotal': subtotal,
            'total_qty': total_qty,
        })


cart_items_view = CartItems.as_view()
