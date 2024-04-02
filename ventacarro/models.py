from django.db import models
from users.models import UsersModel
from inventario.models import CarroModel

class  VentaModel(models.Model):
    
# Create your models here.
    fechaCompra = models.DateField()
    
    SUCURSAL = (
     ('s1',  'S-001'),
     ('s2', 'S-002'),
     ('s3', 'S-003'),
     ('s4', 'S-004')
    )
    
    sucursal = models.CharField(max_length=10, choices= SUCURSAL)
    usuario = models.ForeignKey(UsersModel, on_delete=models.CASCADE , related_name="ID_User")
    carro_vendido = models.ForeignKey(CarroModel, on_delete=models.CASCADE, related_name="Id_Carro")
    
    def Usuario(self):
        return f"{self.usuario.id} {self.usuario.nombre} {self.usuario.apellido}"

    def Carro(self):
        return f"{self.carro_vendido.marca} {self.carro_vendido.modelo}"