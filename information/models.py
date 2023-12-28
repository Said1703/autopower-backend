from django.db import models
from django.contrib.auth.models import User


class Information(models.Model):

    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    tipo_documento = models.CharField(max_length=50)
    numero_doc = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    telefono = models.FloatField()
    email = models.CharField(max_length=200)
    tipo_vehiculo = models.CharField(max_length=200)
    placa_vehiculo = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"

    class Meta:
        db_table = "information"
