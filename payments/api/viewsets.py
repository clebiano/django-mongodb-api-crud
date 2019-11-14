from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from payments.models import Payment
from .serializers import PaymentSerializer


class PaymentViewSet(ModelViewSet):
    """
    API endpoint that allows payments to be viewed or edited.
    """
    serializer_class = PaymentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['id']

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        queryset = Payment.objects.all()
        if id:
            queryset = Payment.objects.filter(pk=id)
        return queryset
