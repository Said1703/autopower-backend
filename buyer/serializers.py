from rest_framework.serializers import ModelSerializer
from .models import Buyer
from information.serializers import InformationSerializer


class BuyerSerializer(ModelSerializer):
    class Meta:
        model = Buyer
        fields = "__all__"


class InformationbuyerSerializer(ModelSerializer):
    information = InformationSerializer(read_only=True)


class Meta:
    model = Buyer
    fields = ("payment_day", "payment_date", "Information")
