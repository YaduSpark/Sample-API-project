from django.db.models.aggregates import Avg

from rest_framework import filters
from rest_framework import generics
from rest_framework.response import Response

from .serializers import *
# Create your views here.


class ProductList(generics.ListCreateAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['price', 'rating']


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer


class CatagoryList(generics.ListCreateAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']


class CatagoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = category.objects.all()
    serializer_class = CategorySerializer


class ManufacturerList(generics.ListCreateAPIView):
    queryset = manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']


class ManufacturerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class PurchaseList(generics.ListCreateAPIView):
    queryset = PurchaseRecord.objects.all()
    serializer_class = PurchaseSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        avg_quantity = queryset.aggregate(Avg('quantity'))
        print(avg_quantity)
        print(serializer.data)
        return Response(serializer.data)


class PurchaseDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseRecord.objects.all()
    serializer_class = PurchaseSerializer