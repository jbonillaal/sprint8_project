import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Casilla de verificación para construir un histograma
build_histogram = st.checkbox('Construir un histograma')

# Casilla de verificación para construir un gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

# Si se selecciona la casilla de verificación para construir un histograma
if build_histogram:
    # Escribir un mensaje
    st.write('Construyendo un histograma para "odometer"')
    
    # Crear un histograma utilizando Plotly Express
    fig = px.histogram(car_data, x="odometer")
    
    # Mostrar el histograma en Streamlit
    st.plotly_chart(fig, use_container_width=True)

# Si se selecciona la casilla de verificación para construir un gráfico de dispersión
if build_scatter:
    # Escribir un mensaje
    st.write('Construyendo un gráfico de dispersión')
    
    # Crear un gráfico de dispersión utilizando Plotly Express
    fig = px.scatter(car_data, x="odometer", y="price")
    
    # Mostrar el gráfico de dispersión en Streamlit
    st.plotly_chart(fig, use_container_width=True)
