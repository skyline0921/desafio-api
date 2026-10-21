from django.db import models
from django.conf import settings
from registers.models import Company, Client, PaymentMethod, Product

class Sale(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        related_name="sales"
    )

    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        related_name="sales"
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="sales"
    )

    date = models.DateTimeField(auto_now_add=True)

    payment_method = models.ForeignKey(
        PaymentMethod,
        on_delete=models.PROTECT,
        related_name="sales"
    )

class SaleItem(models.Model):

    sale = models.ForeignKey(
        Sale,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="items"
    )

    quantity = models.PositiveIntegerField()

    unit_price = models.DecimalField(max_digits=5, decimal_places=2)