from django.db import models
# from django.contrib.auth.models import User
# from subscription.models import Subscription
from django.core.validators import MaxValueValidator
from information.models import Information


class Buyer(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    information = models.ForeignKey(
        Information, on_delete=models.CASCADE, null=True)
    # subscription = models.OneToOneField(
    #     Subscription, on_delete=models.CASCADE, null=True)
    payment_day = models.PositiveIntegerField(
        validators=[MaxValueValidator(31)], null=True)
    payment_date = models.DateField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.payment_day} {self.payment_date} {self.information} "

    class Meta:
        db_table = "buyer"
