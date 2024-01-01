from rest_framework.serializers import ModelSerializer
from .models import Buy


class BuySerializer(ModelSerializer):
    class Meta:
        model = Buy
        fields = "__all__"
