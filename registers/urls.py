from django.urls import path
from .views import MarkList, MarkDetail, ProductList, ProductDetail, ColectionList, ColectionDetail , ClientList, ClientDetail, CompanyDetail, CompanyList, PaymentMethodDetail, PaymentMethodList

urlpatterns = [
    path("marks/", MarkList.as_view()),
    path("marks/<int:pk>/", MarkDetail.as_view()),
    path("products/", ProductList.as_view()),
    path("products/<int:pk>/", ProductDetail.as_view()),
    path("colections/", ColectionList.as_view()),
    path("colections/<int:pk>/", ColectionDetail.as_view()),
    path("clients/", ClientList.as_view()),
    path("clients/<int:pk>/", ClientDetail.as_view()),
    path("companys/", CompanyList.as_view()),
    path("companys/<int:pk>/", CompanyDetail.as_view()),
    path("paymentMethods/", PaymentMethodList.as_view()),
    path("paymentMethods/<int:pk>/", PaymentMethodDetail.as_view())
]