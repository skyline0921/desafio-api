from rest_framework import viewsets
from .models import Mark, Product, Colection, Client, Company, PaymentMethod
from .serializers import MarkSerializer, ProductSerializer, ColectionSerializer, ClientSerializer, CompanySerializer, PaymentMethodSerializer

# Create your views here.

class MarkViewSet(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ColectionViewSet(viewsets.ModelViewSet):
    queryset = Colection.objects.all()
    serializer_class = ColectionSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer