from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ProductSerializer
from .models import Product
from rest_framework import permissions
from .permission import IsOwner


class ProductListAPIView(ListCreateAPIView):
    """_summary_

    Args:
        ListCreateAPIView (_type_): _list and create api for product get and create the product_

    Returns:
        _type_: _description_
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    """_summary_

    Args:
        RetrieveUpdateDestroyAPIView (_type_): _retrive update and delete by id_

    Returns:
        _type_: _python object_
    """
    serializer_class = ProductSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Product.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)