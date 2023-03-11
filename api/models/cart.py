from django.db import models
from django.contrib.auth.models import User as UserModel


class Cart(models.Model):
    user = models.ForeignKey(
        UserModel, related_name='cart_user', on_delete=models.CASCADE)
