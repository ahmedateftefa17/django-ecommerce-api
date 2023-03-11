from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.permissions import AllowAny

from ..serializers.register import register


class register(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = register
