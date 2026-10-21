from django.db import models

class Mark(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Colection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    mark = models.ForeignKey(
        Mark,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    colection = models.ForeignKey(
        Colection,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    telephone = models.CharField(max_length=14)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100)
    tax_id = models.CharField(max_length=18, unique=True)
    active = models.BooleanField(max_length=100)

    def __str__(self):
        return self.name

class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=280, blank=True)
    active = models.BooleanField(max_length=100)

    def __str__(self):
        return self.name