from django.shortcuts import render
from ventacarro.models import VentaModel
import plotly.express as px
import pandas as pd

def ir(request) :
     
    ventas = VentaModel.objects.all()
    context ={
             "Allventas": ventas
     }
    return render(request, "ventacarro/index.html", context)

