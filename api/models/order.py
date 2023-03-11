from django.db import models
from django.contrib.auth.models import User as UserModel


class Order(models.Model):
    user = models.ForeignKey(
        UserModel, related_name='order_user', on_delete=models.CASCADE)
