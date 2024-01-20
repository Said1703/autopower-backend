from rest_framework.viewsets import ModelViewSet
from .models import Information, Paises, Autos
from .serializers import InformationSerializer, PaisesSerializer, AutosSerializer
from django.views import View
from django.http import JsonResponse
from rest_framework.decorators import api_view
# from rest_framework.permissions import IsAuthenticated


class InformationViewSet(ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    # pagintation_class = [IsAuthenticated]


class PaisesViewSet(ModelViewSet):
    queryset = Paises.objects.all()
    serializer_class = PaisesSerializer


class AutosViewSet(ModelViewSet):
    queryset = Autos.objects.all()
    serializer_class = AutosSerializer


@api_view(["POST"])
def login(request):
    validation = Information.objects.filter(numero_doc=request.data["numero_doc"]).filter(
        tipo_documento=request.data["tipo_documento"]).filter(placa_vehiculo=request.data["placa_vehiculo"])

    serializer = InformationSerializer(validation, many=True)

    return JsonResponse({"ok": True, "data": serializer.data})
