from django.db import models


class Subscription(models.Model):
    PRECIO_PLAN = [
        ('10', 'Basic'),
        ('20', 'Gold'),
        ('30', 'Platinum'),
    ]
    precio = models.CharField(
        max_length=50, choices=PRECIO_PLAN, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.precio}"

    class Meta:
        db_table = "subscription"
