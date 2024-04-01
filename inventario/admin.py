from django.contrib import admin
from inventario.models import CarroModel
# Register your models here.
class InventarioAdmin(admin.ModelAdmin):
        list_display = [ "id", "marca", "modelo",  "colorCarro", "precio"]
        list_search = ["marca"]

    
admin.site.register(CarroModel, InventarioAdmin)

