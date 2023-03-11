from django.db import models

from ..models import Product as ProductModel
from ..models import Cart as CartModel


class CartItem(models.Model):
    cart = models.ForeignKey(
        CartModel, related_name='cart', on_delete=models.CASCADE)
    product = models.ForeignKey(
        ProductModel, related_name='cart_product', on_delete=models.CASCADE)
    qty = models.DecimalField(max_digits=12, decimal_places=3)
