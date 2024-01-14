from rest_framework.viewsets import ModelViewSet
from .models import Information, Paises, Autos
from .serializers import InformationSerializer, PaisesSerializer, AutosSerializer
from rest_framework.permissions import IsAuthenticated


class InformationViewSet(ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    permission_classes = [IsAuthenticated]


class PaisesViewSet(ModelViewSet):
    queryset = Paises.objects.all()
    serializer_class = PaisesSerializer


class AutosViewSet(ModelViewSet):
    queryset = Autos.objects.all()
    serializer_class = AutosSerializer
