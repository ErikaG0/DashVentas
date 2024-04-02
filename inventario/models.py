from django.db import models

class CarroModel(models.Model):
    MARCAS = (
    ('Toyota', 'Toyota'),
    ('Honda', 'Honda'),
    ('Ford', 'Ford'),
    ('Chevrolet', 'Chevrolet'),
    ('Nissan', 'Nissan'),
    )
    marca = models.CharField(max_length=50, choices=MARCAS, default= '' )
    MODELOS = (
    ('Sedane', 'Sedane'),
    ('Camioneta', 'Camioneta'),
    ('Híbrido', 'Híbrido')
    )
    modelo = models.CharField(max_length=50, choices=MODELOS, default= '' )
    precio = models.IntegerField()
    COLORES = (
        ('rojo', 'Rojo'),
        ('negro', 'Negro'),
        ('blanco', 'Blanco'),
         ('gris', 'Gris')
    )
    colorCarro = models.CharField(max_length=10, choices=COLORES, default= '' )