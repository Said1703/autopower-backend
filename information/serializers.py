from rest_framework.serializers import ModelSerializer
from .models import Information


class InformationSerializer(ModelSerializer):
    class Meta:
        model = Information
        fields = "__all__"
