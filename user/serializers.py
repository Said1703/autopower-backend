from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(ModelSerializer):

    def create(self, validated_data):
        last_name = validated_data.pop("last_name", None)
        email = validated_data.pop("email", None)

        user = User.objects.create(
            **validated_data, last_name=last_name, email=email)
        return user

    class Meta:
        model = User
        fields = ['username', 'last_name', 'email']
