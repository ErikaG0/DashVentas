from django.contrib import admin
from users.models import UsersModel

# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = ["nombre","apellido","paisUser","ciudad","gen","fechNac", "barrio"]
    def formfield_for_choice_field(self, db_field, request, **kwargs):
        if db_field.name == "barrio":
            # Obtén el objeto del usuario actual
            obj = kwargs.get("obj")
            if obj and obj.ciudad:
                # Filtra los barrios según la ciudad seleccionada
                kwargs["choices"] = [(barrio, barrio) for barrio in obj.obtener_barrios()]
        return super().formfield_for_choice_field(db_field, request, **kwargs)
   
   
  
admin.site.register(UsersModel, UsersAdmin)