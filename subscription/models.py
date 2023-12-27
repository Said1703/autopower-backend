from django.db import models


class Subscription(models.Model):
    title = models.CharField(max_length=250)
    price = models.FloatField()
    discount = models.IntegerField(null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.price}"

    class Meta:
        db_table = "subscription"
