from rest_framework.viewsets import ModelViewSet
from .serializers import BuySerializer
from .models import Buy
import requests
from decouple import config


class BuyViewSet(ModelViewSet):
    queryset = Buy.objects.all()
    serializer_class = BuySerializer

    def create(self, request):
        data = {
            'description': 'Gracias por adquirir Autopower',
            'installments': request.data.get('installments'),
            'issuer_id': request.data.get('issuer_id'),
            'payer': {
                'email': request.data.get('payer_email'),
            },
            'payment_method_id': request.data.get('payment_method_id'),
            'token': request.data.get('token'),
            'transaction_amount': request.data.get('amount')
        }

        response = requests.post(
            'https://api.mercadopago.com/v1/buy',
            json=data,
            headers={
                'Authorization': f'Bearer {config("MERCADOPAGO_ACCESS_TOKEN")}',
                'Content-Type': 'application/json'
            }
        )

        return super().create(request)
