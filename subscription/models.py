from django.db import models


class Subscription(models.Model):

    title = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return f"{self.precio}"

    class Meta:
        db_table = "subscription"