from rest_framework import serializers

from ..models import Product as ProductModel


class Product(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ('name', 'price')
