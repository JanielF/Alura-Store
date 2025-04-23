#Importación de datos
import pandas as pd
from matplotlib import pyplot as plt
import os


url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda = pd.read_csv(url)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4) 

# df = pd.DataFrame(data=tienda)
# print(df)

#El total de filas y columnas de las tiendas es de [2359 rows y 12 columns]

print(tienda.head()) #Se le puede colocar un numero para limiar las filas

tiendas_completas = [tienda,tienda2,tienda3,tienda4]

#Analisis de Facturación
for i, t in enumerate(tiendas_completas, 1):
    ingresos = t["Precio"].sum()
    ingresos = "${:,.2f}".format(ingresos) #Formateamos el costo de envio
    print(f"\n Ingresos de la Tienda {i}: {ingresos}") #Imprimimos los ingresos de cada tienda

#Ventas por categoría
for i, t in enumerate(tiendas_completas, 1):
    ventas = t.groupby("Categoría del Producto")["Precio"].sum()#Agrupamos por categoría y sumamos el precio
    ventas = ventas.sort_values(ascending=False)
    print(f"\n Ventas Tienda {i} por Categoria")
    print(ventas) #Imprimimos las ventas por categoría de cada tienda

#Valoración media por tienda

for i, t in enumerate(tiendas_completas, 1):
    valoracion = t["Calificación"].mean().round(2) #Agrupamos por tienda y sacamos la media de la valoración
    print(f"\n Valoración media de la Tienda {i}: {valoracion}")

#Productos mas y menos vendidos por tienda

for i, t in enumerate(tiendas_completas, 1):
    productos_max_min = t["Producto"].value_counts()
    print(f"\n Producto más y menos vendidos de la Tienda {i}: {productos_max_min}")

#Costo promedio del envio por tienda

for i, t in enumerate(tiendas_completas, 1):
    costo_envio = t["Costo de envío"].mean()
    costo_envio = round(costo_envio, 2)
    costo_envio = "${:,.2f}".format(costo_envio) #Formateamos el costo de envio
    print(f"\n El costo promedio de envio de la tienda {i} es: {costo_envio}")


#Generación de graficos para visualizar los datos

#Ingresos de las tiendas en grafico

# Datos

import matplotlib.pyplot as plt

# Crear carpeta "Graficos" si no existe
if not os.path.exists("Graficos"):
    os.makedirs("Graficos")

# Datos
x = ["Tienda 1", "Tienda 2", "Tienda 3", "Tienda 4"]
y = [tienda["Precio"].sum(), tienda2["Precio"].sum(), tienda3["Precio"].sum(), tienda4["Precio"].sum()]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Crear gráfico
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(x, y, color=colors, edgecolor='black')

# Título y etiquetas
ax.set_title("Ingresos totales por tienda (2020–2023)", fontsize=16, fontweight='bold')
ax.set_xlabel("Tiendas", fontsize=12)
ax.set_ylabel("Ingresos totales", fontsize=12)

# Etiquetas encima de cada barra
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1e7, 
            f"${yval:,.0f}", ha='center', va='bottom', fontsize=10, fontweight='bold')

# Estilo del eje Y
ax.grid(axis="y", linestyle="--", alpha=0.7)
ax.set_axisbelow(True)

# Rotación de etiquetas
plt.xticks(rotation=0)

# Ajuste visual
plt.tight_layout()

# Guardar gráfico en carpeta "Graficos"
plt.savefig("Graficos/ingresos_totales_tiendas.png", dpi=300, bbox_inches='tight')

# Mostrar gráfico
plt.show()

#Valoracion media por tienda en grafico

# Paso 1: Crear los datos

# Crear carpeta "Graficos" si no existe
if not os.path.exists("Graficos"):
    os.makedirs("Graficos")

# Datos
x1 = ["Tienda 1", "Tienda 2", "Tienda 3", "Tienda 4"]
y1 = [
    tienda["Calificación"].mean(),
    tienda2["Calificación"].mean(),
    tienda3["Calificación"].mean(),
    tienda4["Calificación"].mean()
]

# Colores personalizados
colors1 = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Crear gráfico de pastel
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(
    y1,
    labels=x1,
    colors=colors1,
    autopct="%1.1f%%",
    startangle=90,
    shadow=True
)

# Título
ax.set_title("Valoración media por tienda (2020–2023)", fontsize=16, fontweight='bold')

# Ajuste del layout
plt.tight_layout()

# Guardar el gráfico en carpeta "Graficos"
plt.savefig("Graficos/valoracion_media_tiendas.png", dpi=300, bbox_inches='tight')

# Mostrar el gráfico
plt.show()


#categoria mas vendida por tienda en grafico horizontal bar

# Datos

# 1. Contar productos por categoría para cada tienda
ventas1 = tienda["Categoría del Producto"].value_counts()
ventas2 = tienda2["Categoría del Producto"].value_counts()
ventas3 = tienda3["Categoría del Producto"].value_counts()
ventas4 = tienda4["Categoría del Producto"].value_counts()

# 2. Unir en un solo DataFrame
ventas_df = pd.DataFrame({
    "Tienda 1": ventas1,
    "Tienda 2": ventas2,
    "Tienda 3": ventas3,
    "Tienda 4": ventas4
}).fillna(0)

# 3. Convertir a enteros
ventas_df = ventas_df.astype(int)

# 4. Agregar columna de total por categoría y ordenar de menor a mayor
ventas_df["Total"] = ventas_df.sum(axis=1)
ventas_df = ventas_df.sort_values("Total", ascending=False)

# 5. Eliminar la columna de total (solo era para ordenar)
ventas_df.drop(columns="Total", inplace=True)

# 6. Crear carpeta "Graficos" si no existe
if not os.path.exists("Graficos"):
    os.makedirs("Graficos")

# 7. Crear gráfico de barras horizontales apiladas
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
ventas_df.plot(kind='barh', stacked=True, color=colors, figsize=(10, 6))

# 8. Personalización
plt.title("Productos vendidos por categoría y tienda", fontsize=16, fontweight="bold")
plt.xlabel("Productos vendidos")
plt.ylabel("Categorías")
plt.legend(title="Tiendas", loc="upper right")
plt.tight_layout()

# 9. Guardar gráfico en la carpeta
plt.savefig("Graficos/productos_vendidos_por_categoria.png", dpi=300, bbox_inches='tight')

# 10. Mostrar gráfico
plt.show()
