
from rest_framework.routers import DefaultRouter
from .views import (
    MarkViewSet,
    ProductViewSet,
    ColectionViewSet,
    ClientViewSet,
    CompanyViewSet,
    PaymentMethodViewSet,
    UserCreateView,
    LoginView
)
from django.urls import path

router = DefaultRouter()

router.register("marks", MarkViewSet, basename="mark")
router.register("products", ProductViewSet, basename="product")
router.register("colections", ColectionViewSet, basename="colection")
router.register("clients", ClientViewSet, basename="client")
router.register("companys", CompanyViewSet, basename="company")
router.register("paymentMethods", PaymentMethodViewSet, basename="payment-method")

urlpatterns = router.urls + [
    path("register/", UserCreateView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
]