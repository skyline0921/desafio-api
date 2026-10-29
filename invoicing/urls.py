from django.urls import path
from .views import SaleViewsets, SaleItemViewsets

urlpatterns = [
    path("sale/", SaleViewsets.as_view()),
    path("sale-item/", SaleItemViewsets.as_view())
]