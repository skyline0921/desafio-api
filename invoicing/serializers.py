from rest_framework import serializers
from .models import SaleItem, Sale
from django.db import models
class SaleItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleItem
        fields = "__all__"
        extra_kwargs = {
            "id": {"read_only": False, "required": False}
        }

class SaleSerializer(serializers.ModelSerializer):
    items = SaleItemSerializer(many=True)
    class Meta:
        model = Sale
        fields = "__all__"
        read_only_fields = ["status"]

    def create(self, validated_data):
        items_data = validated_data.pop("items")

        sale = Sale.objects.create(**validated_data)

        for item_data in items_data:
            SaleItem.objects.create(
                sale=sale,
                **item_data
            )

        return sale

    def update(self, instance, validated_data):
        items_data = validated_data.pop("items", [])

        for item_data in items_data:
            item_id = item_data.get("id")

            if item_id:
                item = SaleItem.objects.filter(id=item_id, sale=instance).first()

                if item:
                    item.quantity = item_data["quantity"]
                    item.save()
                else:
                    SaleItem.objects.create(
                        sale=instance,
                        **item_data
                    )
            else:
                SaleItem.objects.create(
                    sale=instance,
                    **item_data
                )

        for field, value in validated_data.items():
            setattr(instance, field, value)

        instance.save()

        return instance