from django.db import models

from ..models import ProductModel
from ..models import CartModel


class CartItem(models.Model):
    cart = models.ForeignKey(
        CartModel, related_name='cart', on_delete=models.CASCADE)
    product = models.ForeignKey(
        ProductModel, related_name='cart_product', on_delete=models.CASCADE)
    qty = models.DecimalField(max_digits=12, decimal_places=3)
