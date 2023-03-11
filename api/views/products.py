from rest_framework import generics
from rest_framework.response import Response

from ..serializers.Product import Product as ProductSerializer
from ..models.Product import Product as ProductModel


class products(generics.ListAPIView):
    queryset = ProductModel.objects
    serializer_class = ProductSerializer

    def list(self, request):
        queryset = self.get_queryset()

        if 'search_term' in request.GET and len(request.GET.get('search_term')) > 0:
            queryset = queryset.filter(
                name__contains=request.GET.get('search_term'))

        if 'sort_by_price' in request.GET and request.GET.get('sort_by_price') == 'htl':
            queryset = queryset.order_by('-price')

        if 'search_term' in request.GET and request.GET.get('sort_by_price') == 'lth':
            queryset = queryset.order_by('price')

        queryset = queryset.all()

        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data)
