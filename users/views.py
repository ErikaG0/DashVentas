from django.shortcuts import render
from  users.models import UsersModel
from django.db.models import Func, F, ExpressionWrapper, IntegerField
from datetime import date
import plotly.express as px
import pandas as pd
import plotly.offline as pyo 

def calcular_edad(fecha_nacimiento):
    hoy = date.today()
    edad = hoy.year - fecha_nacimiento.year - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

def comienza(request):
    usuarios = UsersModel.objects.all()
    for usuario in usuarios:
        usuario.edad = calcular_edad(usuario.fechNac)
    
    user_data = [
     {
     "Edad": calcular_edad(usuario.fechNac),
      "Gen": usuario.get_gen_display(),
      "Barrio": usuario.get_barrio_display()
     }
     for usuario in usuarios
   ]
    df = pd.DataFrame(user_data)
    graficoB = px.pie(df, names="Barrio", title="Distribución Barrio")
    graficoG = px.pie(df, names="Gen", title="Distribución Genero")
   
    miHtml = graficoB.to_html( full_html = False) 
    graficaGen= graficoG.to_html(full_html= False)
    context = {
        "Alluser": usuarios,
        "graficaU" : miHtml,
        "graficaG" : graficaGen
    }
    
    
    return render(request, "users/index.html", context)
