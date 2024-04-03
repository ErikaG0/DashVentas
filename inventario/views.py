from django.shortcuts import render
from  inventario.models import CarroModel
import plotly.express as px
import pandas as pd

def saludar(request) :
    carros = CarroModel.objects.all()  #consulta select * from
    
    carros_data = [
        {
            "Marca": carro.marca,
            "modelo": carro.get_modelo_display(),
            "colorCarro": carro.colorCarro,
            "Precio": carro.precio
        }
        for carro in carros
    ]
    df= pd.DataFrame(carros_data)
    

    grafico = px.scatter(df, x="Marca", y="Precio", color="modelo", title="Precio Por Marca y Modelo")
    miHtml = grafico.to_html( full_html = False)
    
    grafico2 = px.pie(df, names="colorCarro", values="Precio", title="Colores Carros")
    miHtml2 = grafico2.to_html( full_html = False)
    
    context = {
       "Allcarros" : carros,
       "graficas"  : miHtml,
        "grafica2"  : miHtml2,
    }
   
    return render(request, "inventario/index.html",  context)