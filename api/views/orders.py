from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from ..models import Cart as CartModel, CartItem as CartItemModel, Order as OrderModel, OrderItem as OrderItemModel
from ..serializers import OrderItem as OrderItemSerializer


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

        order_items = OrderItemModel.objects.filter(order=order.id).all()
        order_items_serializer = OrderItemSerializer(order_items, many=True)

        subtotal = 0
        total_qty = 0
        for order_item in order_items:
            subtotal += order_item.qty * order_item.product.price
            total_qty += order_item.qty

        return Response({
            'items': order_items_serializer.data,
            'subtotal': subtotal,
            'total_qty': total_qty,
        })

    def list(self, request):
        user = request.user

        orders = OrderModel.objects.filter(user=user.id).all()

        orders_list = []

        for order in orders:
            order_items = OrderItemModel.objects.filter(order=order.id).all()
            order_items_serializer = OrderItemSerializer(
                order_items, many=True)

            subtotal = 0
            total_qty = 0
            for order_item in order_items:
                subtotal += order_item.qty * order_item.product.price
                total_qty += order_item.qty

            orders_list.append({
                'id': order.id,
                'items': order_items_serializer.data,
                'subtotal': subtotal,
                'total_qty': total_qty,
            })

        return Response(orders_list)


class OrdersPK(generics.RetrieveAPIView):
    def retrieve(self, request, pk):
        user = request.user

        try:
            order = OrderModel.objects.filter(pk=pk, user=user.id).get()
        except:
            return Response({
                'order': 'Order does not exist!',
            }, status=status.HTTP_404_NOT_FOUND)

        order_items = OrderItemModel.objects.filter(order=order.id).all()
        order_items_serializer = OrderItemSerializer(order_items, many=True)

        subtotal = 0
        total_qty = 0
        for order_item in order_items:
            subtotal += order_item.qty * order_item.product.price
            total_qty += order_item.qty

        return Response({
            'items': order_items_serializer.data,
            'subtotal': subtotal,
            'total_qty': total_qty,
        })


orders_view = Orders.as_view()
orders_pk_view = OrdersPK.as_view()
