from rest_framework.viewsets import ModelViewSet
from .models import Information
from .serializers import InformationSerializer
from rest_framework.permissions import IsAuthenticated


class InformationViewSet(ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    permission_classes = [IsAuthenticated]
