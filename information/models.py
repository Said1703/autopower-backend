from django.db import models
from django.contrib.auth.models import User
from subscription.models import Subscription


class Paises(models.Model):
    PAIS_CHOICES = [
        ('PE', 'Perú'),
        ('VE', 'Venezuela'),
        ('MX', 'México'),
        ('EC', 'Ecuador'),
        ('AR', 'Argentina'),
        ('UY', 'Uruguay'),
        ('CL', 'Chile'),
        ('BO', 'Bolivia'),
        ('PY', 'Paraguay'),
        ('BR', 'Brasil'),
        ('CO', 'Colombia'),
    ]
    pais = models.CharField(max_length=2, choices=PAIS_CHOICES, null=True)

    class Meta:
        db_table = "country"


class Autos(models.Model):
    AUTOS_CHOICES = [
        ('SEDAN', 'Sedán'),
        ('HATCHBACK', 'Hatchback'),
        ('COUPE', 'Coupé'),
        ('STATION_WAGON', 'Station wagon'),
        ('SUV', 'Suv'),
        ('CROSSOVER', 'Crossover'),
        ('CONVERTIBLE', 'Convertible'),
        ('4X4', '4x4'),
        ('OTROS', 'Otros'),
    ]
    autos = models.CharField(max_length=30, choices=AUTOS_CHOICES, null=True)

    class Meta:
        db_table = "autos"


class Information(models.Model):
    subscription = models.OneToOneField(
        Subscription, on_delete=models.CASCADE, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    TIPO_DOCUMENTO_CHOICES = [
        ('DNI', 'Documento Nacional de Identidad'),
        ('PAS', 'Pasaporte'),
        ('CAR', 'Carnet de extranjeria'),
    ]
    tipo_documento = models.CharField(
        max_length=50, choices=TIPO_DOCUMENTO_CHOICES, blank=True)
    numero_doc = models.CharField(max_length=50, unique=True, blank=True)
    pais = models.CharField(
        max_length=2, choices=Paises.PAIS_CHOICES, default='PE', null=True,)
    telefono = models.CharField(max_length=10, unique=True, blank=True)
    tipo_vehiculo = models.CharField(
        max_length=30, choices=Autos.AUTOS_CHOICES, default='SEDAN', null=True,)
    placa_vehiculo = models.CharField(max_length=10, unique=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} {self.subscription} {self.placa_vehiculo} {self.tipo_documento} {self.numero_doc}"

    class Meta:
        db_table = "information"
