from rest_framework import generics
from .models import Sale, SaleItem
from .serializers import SaleItemSerializer, SaleSerializer
from django.db.models import Sum, F
from invoicing import SaleItem
# Create your views here.

class SaleItemList(generics.ListCreateAPIView):
    queryset = SaleItem.objects.value()
    serializer_class = SaleItemSerializer    
class SaleItemDetail(generics.RetrieveDestroyAPIView):
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer
class SaleList(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
class SaleDetail(generics.RetrieveDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer