from django.shortcuts import render
from ventacarro.models import VentaModel
from inventario.models import CarroModel
import plotly.express as px
import pandas as pd
import calendar

def ir(request):
    ventas = VentaModel.objects.all()

    ventas_data = [
        {
            "FechaCompra": pd.to_datetime(venta.fechaCompra),
            "Sucursal": venta.get_sucursal_display(),
            "Valor": venta.carro_vendido.precio,
            "Modelo":venta.carro_vendido.get_modelo_display()
        }
        for venta in ventas
    ]
    df = pd.DataFrame(ventas_data)

  
    df['Mes'] = df['FechaCompra'].dt.month
    df['Año'] = df['FechaCompra'].dt.year

    # Crear un diccionario  nombres de mes
    meses = {i + 1: calendar.month_abbr[i] for i in range(1, 13)}
    df['Mes'] = df['Mes'].map(meses)
    df_grouped = df.groupby(['Año', 'Mes', 'Sucursal'])['Valor'].sum().reset_index()
    grafico = px.area(df_grouped, x="Mes", y="Valor", color="Sucursal", facet_row="Año",
                      title="Ventas por Mes y Sucursal")

    miHtml = grafico.to_html(full_html=False)
    
    graficoModelo = px.pie(df, names="Modelo", title="Modelo Vendidos")
    miHtml2 = graficoModelo.to_html(full_html=False)
    context = {
        "Allventas": ventas,
        "graficaV": miHtml,
        "graficaPie": miHtml2
    }
    return render(request, "ventacarro/index.html", context)
