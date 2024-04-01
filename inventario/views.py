from django.shortcuts import render
from  inventario.models import CarroModel
import plotly.express as px
import pandas as pd

def saludar(request) :
    carros = CarroModel.objects.all()  #consulta select * from

    df = pd.DataFrame({
        "marca": ["ferrari", "mazana","pero"],
        "cantidad":[20 , 12 ,14],
        "pais":["arge", "brazil", "col"]
    })
 
    grafico = px.bar(df, x = "marca", y="cantidad", color="pais")
    miHtml = grafico.to_html( full_html = False)

    context = {
        "nombre" : "coco",
        "Allcarros" : carros,
        "graficas"  : miHtml
    }
    return render(request, "inventario/index.html",  context)

