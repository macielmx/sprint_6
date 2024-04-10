import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Herramienta para la elección de autos usados') #crear de un encabezado

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    st.write('Creando histograma de los autos anunciados para su venta') # escribir un mensaje     
    fig = px.histogram(car_data, x="odometer") # crear un histograma      
    st.plotly_chart(fig, use_container_width=True) # mostrar un gráfico Plotly interactivo

scatter_button = st.button('Construir gráfico de dispersión') # crear un botón
        
if scatter_button: # al hacer clic en el botón
    st.write('Creando gráfico de despersión de los autos anunciados para su venta') # escribir un mensaje     
    fig = px.scatter(car_data, x="odometer") # crear un histograma      
    st.plotly_chart(fig, use_container_width=True) # mostrar un gráfico Plotly interactivo
