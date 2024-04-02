from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

class UsersModel(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    paisUser = models.CharField(max_length=40, default='Colombia')
    
    GENERO = (
        ('h', 'Hombre'),
        ('m', 'Mujer')  
    )
    gen = models.CharField(max_length=5, choices=GENERO, default='')
    fechNac = models.DateField(blank=True, null=True)
    ciudad = models.CharField(max_length=40, default='Bogota')
 
    BARRIOS = (
        ('barrioB1', 'Chapinero'),
        ('barrioB2', 'Usaquen'), 
        ('barrioB3', 'Suba') ,
        ('barrioB4', 'Kennedy') ,
        ('barrioB5', 'Usme') ,
    )
    barrio = models.CharField(max_length=100, choices=BARRIOS)