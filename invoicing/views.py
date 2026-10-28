from rest_framework import viewsets
from .models import Sale, SaleItem
from .serializers import SaleItemSerializer, SaleSerializer
from invoicing import SaleItem
# Create your views here.

class SaleItemList(viewsets.ModelViewSet):
    queryset = SaleItem.objects.value()
    serializer_class = SaleItemSerializer    
class SaleList(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer