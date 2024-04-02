
from django.contrib import admin
from django.urls import path
from  inventario.views import saludar  #"importar controlador o vista "
from users.views import comienza
from  ventacarro.views import ir
urlpatterns = [
    path('admin/', admin.site.urls),
     path('inventario/',  saludar , name='inventarioHtml'),
     path('users/', comienza, name='usuarioHtml'),
     path('ventacarro/', ir, name='ventaHtml'),
     
]
