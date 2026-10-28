from rest_framework import viewsets
from .models import Mark, Product, Colection, Client, Company, PaymentMethod
from .serializers import MarkSerializer, ProductSerializer, ColectionSerializer, ClientSerializer, CompanySerializer, PaymentMethodSerializer

# Create your views here.

class MarkList(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer

class ProductList(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ColectionList(viewsets.ModelViewSet):
    queryset = Colection.objects.all()
    serializer_class = ColectionSerializer

class ClientList(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientList(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class CompanyList(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class PaymentMethodList(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer