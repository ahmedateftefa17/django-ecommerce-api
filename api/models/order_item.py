from django.db import models

from ..models import ProductModel
from ..models import OrderModel


class OrderItem(models.Model):
    order = models.ForeignKey(
        OrderModel, related_name='order', on_delete=models.CASCADE)
    product = models.ForeignKey(
        ProductModel, related_name='order_product', on_delete=models.CASCADE)
    qty = models.DecimalField(max_digits=12, decimal_places=3)
