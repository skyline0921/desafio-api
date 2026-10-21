from django.contrib import admin
from .models import Mark, Product, Colection, Client, Company, PaymentMethod
from invoicing.models import Sale, SaleItem

# Register your models here.

admin.site.register(Mark),
admin.site.register(Product),
admin.site.register(Colection),
admin.site.register(Client),
admin.site.register(Company),
admin.site.register(PaymentMethod),
admin.site.register(Sale),
admin.site.register(SaleItem)