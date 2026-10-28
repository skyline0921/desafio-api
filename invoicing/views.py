from rest_framework import viewsets
from .models import Sale, SaleItem
from .serializers import SaleItemSerializer, SaleSerializer
from invoicing import SaleItem
# Create your views here.

class SaleItemViewsets(viewsets.ModelViewSet):
    queryset = SaleItem.objects.value()
    serializer_class = SaleItemSerializer    
class SaleViewsets(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer