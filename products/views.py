from rest_framework import filters

from rest_framework import generics

from .serializers import *
# Create your views here.


class ProductList(generics.ListCreateAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['price', 'rating']


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer


class CatagoryList(generics.ListCreateAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']


class CatagoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer


class manufacturerList(generics.ListCreateAPIView):
    queryset = manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']


class manufacturerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
