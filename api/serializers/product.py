from rest_framework import serializers

from ..models.product import Product


class Product(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price')
