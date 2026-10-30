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
                {"detail": "Esta venda já está finalizada."},
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

    def update(self, request, *args, **kwargs):
        sale = self.get_object()

        if sale.status == Sale.Status.FINISHED:
            return Response(
                {"detail": "Não é possível alterar uma venda finalizada."},
                status=status.HTTP_400_BAD_REQUEST
        )

        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        sale = self.get_object()

        if sale.status == Sale.Status.FINISHED:
            return Response(
                {"detail": "Não é possível alterar uma venda finalizada."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        sale = self.get_object()

        if sale.status == Sale.Status.FINISHED:
            return Response(
                {"detail:" "Não é possível excluir uma venda finalizada"} ,
                status=status.HTTP_400_BAD_REQUEST
        )
        return super().destroy(request, *args, **kwargs)

class SaleItemViewsets(viewsets.ModelViewSet):
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer

    def update(self, request, *args, **kwargs):
            saleItem = self.get_object()
    
            if saleItem.status == SaleItem.Status.FINISHED:
                return Response(
                    {"detail": "Não é possível alterar uma venda finalizada."},
                    status=status.HTTP_400_BAD_REQUEST
            )
    
            return super().update(request, *args, **kwargs)
                    
    def destroy(self, request, *args, **kwargs):
            saleItem = self.get_object()
    
            if saleItem.status == SaleItem.Status.FINISHED:
                return Response(
                    {"detail:" "Não é possível excluir uma venda finalizada"} ,
                    status=status.HTTP_400_BAD_REQUEST
            )
            return super().destroy(request, *args, **kwargs)