from django.urls import path
from .views import SaleList, SaleDetail, SaleItemList, SaleItemDetail

urlpatterns = [
    path("sale/", SaleList.as_view()),
    path("sale/<int:pk>/", SaleDetail.as_view()),
    path("sale-item/", SaleItemList.as_view()),
    path("sale-item/<int:pk>/", SaleItemDetail.as_view())
]