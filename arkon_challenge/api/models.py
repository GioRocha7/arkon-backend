from django.db import models
from datetime import datetime,date
# Create your models here.
class Evento(models.Model):
    key_evento =models.CharField(max_length=10)
    Nombre=models.CharField(max_length=200)
    fecha_inicio=models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    hora_inicio=models.TimeField(auto_now_add=False,auto_now=False,blank=True,null=True)
    fecha_fin=models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    hora_fin=models.TimeField(auto_now_add=False,auto_now=False,blank=True,null=True)
    max_boletos=models.IntegerField()
    fecha_creacion=models.DateField(auto_now_add=True)
    hora_creacion=models.TimeField(auto_now_add=True)
   

class Boleto(models.Model):
    id_evento=models.ForeignKey(Evento, on_delete=models.CASCADE)
    key_boleto =models.CharField(max_length=10)
    fecha_compra=models.DateField(auto_now_add=True)
    hora_compra=models.TimeField(auto_now_add=True)
    comprador=models.CharField(max_length=200)
    status_canjeo=models.BooleanField(default=False)
    status_active=models.BooleanField(default=False)