from django.db import models
from django.contrib.auth.models import User
from subscription.models import Subscription
from information.models import Information
from django.core.validators import MaxValueValidator


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    subscription = models.OneToOneField(
        Subscription, on_delete=models.CASCADE, null=True)
    information = models.OneToOneField(
        Information, on_delete=models.CASCADE, null=True)
    payment_day = models.PositiveIntegerField(
        validators=[MaxValueValidator(31)], null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.first_name

    class Meta:
        db_table = "buyer"
