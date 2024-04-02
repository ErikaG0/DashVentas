from django.contrib import admin
from   ventacarro.models import VentaModel
# Register your models here.
class VentaAdmin(admin.ModelAdmin):
        list_display =["fechaCompra","sucursal", "Usuario","Carro"]

admin.site.register(VentaModel, VentaAdmin)