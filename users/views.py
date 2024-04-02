from django.shortcuts import render
from  users.models import UsersModel
from django.db.models import Func, F, ExpressionWrapper, IntegerField
from datetime import date
import plotly.express as px
import pandas as pd

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
      "paisUser": usuario.paisUser,
      "ciudad": usuario.ciudad,
      "gen": usuario.gen,
      "barrio": usuario.barrio
     }
     for usuario in usuarios
   ]
    df = pd.DataFrame(user_data)
    grafico= px.bar(df, x="barrio", y="gen", color="ciudad", barmode="group", title="Precio por marca y color")
    miHtml = grafico.to_html( full_html = False)
   
    context = {
        "Alluser": usuarios,
        "graficaU" : miHtml
    }
    
    return render(request, "users/index.html", context)
