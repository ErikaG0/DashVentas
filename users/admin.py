from django.contrib import admin
from users.models import UsersModel

# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    list_display = ["nombre","apellido","paisUser","ciudad","gen","fechNac", "barrio"]
    
  
admin.site.register(UsersModel, UsersAdmin)