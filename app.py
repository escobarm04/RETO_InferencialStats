#Creamos un REPORTE del reto de  estadística inferencial de The learning Gate Data Scientist
#Plataforma streamlit

#Descargamos la paqueteria necesaria
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from PIL import Image
import plotly.express as px

st.set_page_config(page_title='Reto | Costo Póliza de Seguro',
                   page_icon = '🪲', 
                   layout= 'wide', 
                   initial_sidebar_state= 'collapsed')

def main():
    menu = ['Instrucciones', 
            'Clasificar variables', 
            'Ejercico No. 1', 
            'Ejercicio No. 2',
            'Ejercicio No. 3',
            'Ejercicio No. 4',
            'Extra: Ejercicio No. 5',
            'Resumen ejecutivo',]
    navegador = st.sidebar.selectbox('📊 Navegador:', menu)

    if navegador == 'Instrucciones':
        pass

    
    elif navegador == 'Clasificar variables':
        pass
    elif navegador == 'Ejercicio No. 1':
        pass
    elif navegador == 'Ejercicio No. 2':
        pass
    elif navegador == 'Ejercicio No. 3':
        pass
    elif navegador == 'Ejercicio No, 4':
        pass
    elif navegador == 'Extra: Ejercicio No. 5':
        pass
    else:
        pass

main()