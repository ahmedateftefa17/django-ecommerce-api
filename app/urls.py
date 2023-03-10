"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken import views

from api.views import register_api_view, products_api_view, cart_items_api_view, cart_items_pk_api_view, orders_api_view, orders_pk_api_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/token/', views.obtain_auth_token),
    path('api/auth/register/', register_api_view),
    path('api/products/', products_api_view),
    path('api/cart_items/', cart_items_api_view),
    path('api/cart_items/<int:pk>', cart_items_pk_api_view),
    path('api/orders/', orders_api_view),
    path('api/orders/<int:pk>', orders_pk_api_view),
    path('api/auth/', include('rest_framework.urls')),
]
