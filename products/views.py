from rest_framework import generics

from .serializers import *
# Create your views here.


class ProductList(generics.ListCreateAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer


class CatagoryList(generics.ListCreateAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer


class CatagoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer


class manufacturerList(generics.ListCreateAPIView):
    queryset = manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class manufacturerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
