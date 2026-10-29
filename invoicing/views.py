from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Sale, SaleItem
from .serializers import SaleItemSerializer, SaleSerializer
# Create your views here.
class SaleViewsets(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    @action(detail=True, methods=["post"])
    def finalize(self, request, pk=None):
        sale = self.get_object()

        if sale.status == Sale.Status.FINISHED:
            return Response(
                {"detail": "Esta venda já stá finalizada."},
                status=status.HTTP_400_BAD_REQUEST
            )

        sale.status = Sale.Status.FINISHED
        sale.save(update_fields=["status"])

        return Response(
            {
                "detail": "Venda finalizada com sucesso",
                "status": sale.status
            },
            status=status.HTTP_200_OK
        )

class SaleItemViewsets(viewsets.ModelViewSet):
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer