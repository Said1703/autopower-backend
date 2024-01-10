from rest_framework.serializers import ModelSerializer
from .models import Information, Paises


class InformationSerializer(ModelSerializer):
    class Meta:
        model = Information
        fields = "__all__"


class PaisesSerializer(ModelSerializer):
    class Meta:
        model = Paises
        fields = "__all__"
