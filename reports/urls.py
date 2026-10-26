from django.urls import path
from .views import SaleItemTop10, SalesReport

urlpatterns = [
    path(
        "top-products/",
        SaleItemTop10.as_view(),
        name="top-products"
    ),
    path("sales/", SalesReport.as_view(), name="sales-report"),
]
