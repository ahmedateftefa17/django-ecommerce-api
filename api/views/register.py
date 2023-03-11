from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.permissions import AllowAny

from ..serializers.register import Register as RegisterSerializer


class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


register_view = Register.as_view()
