from rest_framework.viewsets import ModelViewSet
from .models import Buyer
from .serializers import BuyerSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


class BuyerViewSet(ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    # permission_classes = [IsAuthenticated]
