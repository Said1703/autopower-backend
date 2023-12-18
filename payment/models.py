from django.db import models


class Payment(models.Model):
    nombre_del_titular = models.CharField(max_length=200)
    numero_de_tarjeta = models.FloatField()
    fecha_de_caducidad = models.DateField()
    cvv = models.CharField(max_length=4)

    class Meta:
        db_table = "payment"
