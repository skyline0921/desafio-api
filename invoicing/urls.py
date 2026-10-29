from rest_framework.routers import DefaultRouter
from .views import SaleViewsets, SaleItemViewsets

router = DefaultRouter()
router.register("sales", SaleViewsets, basename="sales")
router.register("sale-items", SaleItemViewsets, basename="sale-items")

urlpatterns = router.urls