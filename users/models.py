from django.db import models

class UsersModel(models.Model):
    print ("entra model user")
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)

    paisUser= models.CharField(max_length=40,  default= 'Colombia')
    GENERO = (
         ('h', 'Hombre'),
        ('m', 'Mujer')  
        )
    gen = models.CharField(max_length=5, choices=GENERO, default= '' )
    fechNac = models.DateField(blank=True, null=True)
    CIUDAD = (
        ('bogota', 'Bogota'),
        ('medellin', 'Medellin'), 
        ('cali', 'Cali') 
    )
    
    ciudad = models.CharField(max_length=30, choices=CIUDAD, default= '' )
    
    BARRIOS = {
        'bogota': [('barrio1_bogota', 'Barrio1_Bogota'), ('barrio2_bogota', 'Barrio2_Bogota'), ('barrio3_bogota', 'Barrio3_Bogota')],
        'medellin': [('barrio1_medellin', 'Barrio1_Medellin'), ('barrio2_medellin', 'Barrio2_Medellin'), ('barrio3_medellin', 'Barrio3_Medellin')],
        'cali': [('barrio1_cali', 'Barrio1_Cali'), ('barrio2_cali', 'Barrio2_Cali'), ('barrio3_cali', 'Barrio3_Cali')],
    }
    
    barrio = models.CharField(max_length=100, choices=[], default='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.actualizar_opciones_barrio()

    def actualizar_opciones_barrio(self):
        self._meta.get_field('barrio').choices = self.BARRIOS.get(self.ciudad, [])











