from rest_framework.viewsets import ModelViewSet
from .models import Information, Paises
from .serializers import InformationSerializer, PaisesSerializer
from rest_framework.permissions import IsAuthenticated


class InformationViewSet(ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    permission_classes = [IsAuthenticated]


class PaisesViewSet(ModelViewSet):
    queryset = Paises.objects.all()
    serializer_class = PaisesSerializer
