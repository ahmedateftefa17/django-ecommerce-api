from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from ..models import Cart as CartModel, CartItem as CartItemModel, Order as OrderModel, OrderItem as OrderItemModel
from ..serializers import Order as OrderSerializer


class Orders(generics.ListCreateAPIView):
    def create(self, request):
        user = request.user

        try:
            cart = CartModel.objects.filter(user=user.id).get()
        except:
            return Response({
                'cart': 'Cart is empty!',
            }, status=status.HTTP_400_BAD_REQUEST)

        cart_items = CartItemModel.objects.filter(cart=cart.id).all()

        order = OrderModel.objects.create(user=user)
        for cart_item in cart_items:
            OrderItemModel.objects.create(
                order=order, product=cart_item.product, qty=cart_item.qty)
            cart_item.delete()

        cart.delete()

        return Response(OrderSerializer(order, many=False).data)

    def list(self, request):
        user = request.user

        orders = OrderModel.objects.filter(user=user.id).all()

        return Response(OrderSerializer(orders, many=True).data)


class OrdersPK(generics.RetrieveAPIView):
    def retrieve(self, request, pk):
        user = request.user

        try:
            order = OrderModel.objects.filter(pk=pk, user=user.id).get()
        except:
            return Response({
                'order': 'Order does not exist!',
            }, status=status.HTTP_404_NOT_FOUND)

        return Response(OrderSerializer(order).data)


orders_view = Orders.as_view()
orders_pk_view = OrdersPK.as_view()
