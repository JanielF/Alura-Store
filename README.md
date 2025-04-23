# 📶 Analisis de la Eficiencia de las Tiendas del Sr. Juan

El objetivo de este proyecto es realizar un analisis profundo de las Tiendas del Sr. Juan, usando parametros como ***Productos, Categorias, Precio, Calificacion, etc***, de las 4 tiendas del Sr. Juan.

Con este analisis podra elegir de manera concreta la tienda que deberia de vender para poder invertir en su nuevo proyecto.


## 📁 Estructura del Proyecto


```
challenge_store_one/
├── main.py             # Lugar donde se encuentra todo el analisis y graficos que contiene el proyecto
├── README.md           # Documentacón del proyexto

```

## 📊 Tecnologías y Herramientas

- **Lenguaje de programación:** Python
- **Librerías principales:**
  - `pandas` para procesamiento y análisis de datos
  - `matplotlib` para la visualización de datos

## 🚀 Instalación y Uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/JanielF/Alura-Store.git
cd  Alura-store
```
### 2. Crear y activar un entorno virtual (opcional pero recomendado)

```python
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```


### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 📌 Contexto y Objetivo  
La cadena **Alura Store** cuenta con cuatro sucursales y el Sr. Juan desea decidir cuál de ellas vender para lanzar un nuevo emprendimiento.  
**Objetivo:** identificar, con base en datos de ventas y reseñas, la tienda menos eficiente y fundamentar una recomendación clara.

##  📋 Metodología  
1. **Carga y preparación de datos**  
   - Se importaron los archivos CSV de cada tienda usando **Pandas**.  
   - Se validó integridad, consistencia de tipos y ausencia de valores faltantes.

2. **Cálculo de métricas clave**  
   - **Ingresos totales de cada tienda**
   - **Número de ventas por sus categorias** 
   - **Promedio de calificaciones por tienda** 
   - **Productos mas vendidos y menos vendidos**
   - **Costo promedio de envío**

3. **Visualización**  
   - Gráficos (barras, pastel y barras horizontales) implementados con **Matplotlib** para ilustrar comparaciones y tendencias.