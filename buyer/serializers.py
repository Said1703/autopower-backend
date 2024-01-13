from rest_framework.serializers import ModelSerializer
from .models import Buyer


class BuyerSerializer(ModelSerializer):

    class Meta:
        model = Buyer
        fields = "__all__"
