from django.shortcuts import render
from  inventario.models import CarroModel
import plotly.express as px
import pandas as pd

def saludar(request) :
    carros = CarroModel.objects.all()  #consulta select * from
    
    carros_data = [
        {
            "marca": carro.marca,
            "modelo": carro.modelo,
            "colorCarro": carro.colorCarro,
            "precio": carro.precio
        }
        for carro in carros
    ]
    df= pd.DataFrame(carros_data)
    

    grafico = px.bar(df, x="marca", y="precio", color="colorCarro", barmode="group", title="Precio por marca y color")
    miHtml = grafico.to_html( full_html = False)
    context = {
       "Allcarros" : carros,
       "graficas"  : miHtml
        
    }
   
    return render(request, "inventario/index.html",  context)