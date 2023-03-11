from rest_framework import serializers

from ..models.Product import Product


class Product(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'price')
