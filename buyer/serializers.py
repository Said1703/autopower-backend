from rest_framework.serializers import ModelSerializer
from user.serializers import UserSerializer
from subscription.serializers import SubscriptionSerializer
from .models import Buyer


class BuyerSerializer(ModelSerializer):

    class Meta:
        model = Buyer
        fields = "__all__"
