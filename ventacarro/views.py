from django.shortcuts import render
from ventacarro.models import VentaModel
import plotly.express as px
import pandas as pd

def ir(request) :
     
    ventas = VentaModel.objects.all()
    
    ventas_data = [
        {
        "FechaCompra":pd.to_datetime(venta.fechaCompra),
        "Sucursal":venta.get_sucursal_display(),
        "Valor":venta.carro_vendido.precio
        }
        for venta in ventas
    ]
    
    df= pd.DataFrame(ventas_data)
    
    # Extraer el mes de la fecha de compra
    df['Mes'] = df['FechaCompra'].dt.month

    # Agrupar por mes y sucursal y calcular la suma de los valores

    df_grouped = df.groupby(['Mes', 'Sucursal'])['Valor'].sum().reset_index()
    # Crear el gráfico de barras
    grafico = px.bar(df_grouped, x="Mes", y="Valor", color="Sucursal", barmode="group",
    title="Ventas  Mes y Sucursal")

    miHtml = grafico.to_html(full_html=False)
    context ={
             "Allventas": ventas,
             "graficaV" : miHtml
    }
    return render(request, "ventacarro/index.html", context)

