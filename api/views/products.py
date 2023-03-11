from rest_framework import generics
from rest_framework.response import Response

from ..models import ProductModel
from ..serializers import ProductSerializer


class ProductsAPIView(generics.ListAPIView):
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


products_api_view = ProductsAPIView.as_view()
