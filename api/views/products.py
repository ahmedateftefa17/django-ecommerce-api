from rest_framework import generics
from rest_framework.response import Response

from ..serializers.product import Product as ProductSerializer
from ..models.product import Product as ProductModel


class Products(generics.ListAPIView):
    queryset = ProductModel.objects
    serializer_class = ProductSerializer

    def list(self, request):
        queryset = self.get_queryset()

        if len(request.query_params.get('search_term', '')) > 0:
            queryset = queryset.filter(
                name__contains=request.query_params['search_term'])

        if request.query_params.get('sort_by_price', '') == 'htl':
            queryset = queryset.order_by('-price')

        if request.query_params.get('sort_by_price', '') == 'lth':
            queryset = queryset.order_by('price')

        queryset = queryset.all()

        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data)


products_view = Products.as_view()
