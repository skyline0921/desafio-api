from django.db import models
from django.conf import settings
from registers.models import Company, Client, PaymentMethod, Product

class Sale(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDENTE", "Pendente"
        FINISHED = "FINALIZADO", "Finalizado"

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

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING
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