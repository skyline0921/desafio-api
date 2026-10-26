from django.db.models import Sum, F, Min, Max
from invoicing.models import Sale, SaleItem
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.dateparse import parse_date
from decimal import Decimal

# Create your views here.
class SaleItemTop10(APIView):
    def get(self, request):
        start_date = request.query_params.get("start_date")
        final_date = request.query_params.get("final_date")

        start_date = parse_date(start_date) if start_date else None
        final_date = parse_date(final_date) if final_date else None

        date_limits = Sale.objects.aggregate(
            first_date=Min("date"),
            last_date=Max("date")
        )

        if date_limits["first_date"] is None:
            return Response({"products": []})

        first_date = date_limits["first_date"].date()
        last_date = date_limits["last_date"].date()

        if start_date is None:
            start_date = first_date


        if final_date is None:
            final_date = last_date

        
        sale_calc = SaleItem.objects.filter(
            sale__date__date__gte=start_date,
            sale__date__date__lte=final_date
        ).values(
            "product__name"
        ).annotate(
            sale_quantity=Sum("quantity"),
            sale_value=Sum(F("quantity") * F("unit_price"))
        ).order_by("-sale_quantity")[:10]

        return Response({
            "sales":[],
            "start_date": start_date,
            "final_date": final_date,
            "products":sale_calc
        })

class SalesReport(APIView):
    def get(self, request):
        start_date = request.query_params.get("start_date")
        final_date = request.query_params.get("final_date")
        
        start_date = parse_date(start_date) if start_date else None
        final_date = parse_date(final_date) if final_date else None

        start_date = parse_date(start_date) if start_date else None
        final_date = parse_date(final_date) if final_date else None
        
        date_limits = Sale.objects.aggregate(
            first_date=Min("date"),
            last_date=Max("date")
        )
        
        if date_limits["first_date"] is None:
            return Response({
                "start_date": None,
                "final_date": None,
                "sales": []
            })
        
        first_date = date_limits["first_date"].date()
        last_date = date_limits["last_date"].date()
        
        if start_date is None:
            start_date = first_date
        
        if final_date is None:
            final_date = last_date

        sales = Sale.objects.filter(
            date__date__gte=start_date,
            date__date__lte=final_date
        )

        sales = sales.select_related(
            "client",
            "user",
            "payment_method",
        ).prefetch_related(
            "items__product"
        )

        sales_data = []

        for sale in sales:
            items = sale.items.all()
            items_data = []

            for item in items:
                items_data.append({
                    "product": str(item.product),
                    "quantity": item.quantity,
                    "unit_price": item.unit_price,
                    "total": item.quantity * item.unit_price,
                })
            
            sale_total = sum((item.quantity * item.unit_price for item in items), start=Decimal("0.00"))

            sales_data.append({
               "id": sale.id,
                "date": sale.date,
                "client": str(sale.client),
                "user": str(sale.user),
                "payment_method": str(sale.payment_method),
                "total": sale_total,
                "items": items_data
            })

        return Response({
            "start_date": start_date,
            "final_date": final_date,
            "sales": sales_data
        })
