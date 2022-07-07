from rest_framework import generics

from .serializers import *
# Create your views here.


class ProductList(generics.ListCreateAPIView):
    queryset = manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class CatagoryList(generics.ListCreateAPIView):
    queryset = manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class CatagoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class manufacturerList(generics.ListCreateAPIView):
    queryset = manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class manufacturerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
