
from django.contrib import admin
from django.urls import path
from  inventario.views import saludar  #"importar controlador o vista "

urlpatterns = [
    path('admin/', admin.site.urls),
     path('inventario/',  saludar )
]
