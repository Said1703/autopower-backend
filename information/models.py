from django.db import models
from django.contrib.auth.models import User


class Information(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    TIPO_DOCUMENTO_CHOICES = [
        ('DNI', 'Documento Nacional de Identidad'),
        ('PAS', 'Pasaporte'),
        ('CAR', 'Carnet de extranjeria'),
    ]
    tipo_documento = models.CharField(
        max_length=50, choices=TIPO_DOCUMENTO_CHOICES, blank=True)
    numero_doc = models.CharField(max_length=50, unique=True, blank=True)
    pais = models.CharField(max_length=50, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    telefono = models.CharField(max_length=10, unique=True, blank=True)
    tipo_vehiculo = models.CharField(max_length=200, blank=True)
    placa_vehiculo = models.CharField(max_length=10, unique=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.placa_vehiculo} {self.tipo_documento} {self.numero_doc}"

    class Meta:
        db_table = "information"
