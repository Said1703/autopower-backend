from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import Information, Paises, Autos
from subscription.serializers import SubscriptionSerializer
# from buyer.serializers import BuyerSerializer
# from django.contrib.auth import authenticate


class InformationSerializer(ModelSerializer):
    class Meta:
        model = Information
        fields = "__all__"

    # def create(self, validated_data):
    #     numero_doc = validated_data.get('numero_doc')
    #     tipo_documento = validated_data.get('tipo_documento')
    #     placa_vehiculo = validated_data.get('placa_vehiculo')

    #     user = authenticate(request=self.context.get('request'),
    #                         numero_doc=numero_doc,
    #                         tipo_documento=tipo_documento,
    #                         placa_vehiculo=placa_vehiculo)

    #     if not user or not user.is_authenticated:
    #         raise ValidationError(
    #             "Autenticación fallida")

    #     information_instance = Information.objects.create(**validated_data)

    #     return information_instance


class PaisesSerializer(ModelSerializer):
    class Meta:
        model = Paises
        fields = "__all__"


class AutosSerializer(ModelSerializer):
    class Meta:
        model = Autos
        fields = "__all__"


class InformationSubcriptionSerializer(ModelSerializer):

    subscription = SubscriptionSerializer(read_only=True)

    class Meta:
        model = Information
        fields = ("nombre", "apellidos", "placa_vehiculo",
                  "numero_doc", "email", "subscription")


# class InformationBuyerSerializer(ModelSerializer):
#     buyer = BuyerSerializer(read_only=True)

#     class Meta:
#         Model = Information
#         Fields = ("buyer")
