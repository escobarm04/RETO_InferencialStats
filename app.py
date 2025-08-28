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
import scipy as sp
import pingouin as pg
import openpyxl
from scipy.stats import shapiro, probplot
from Reto import *

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
        col1, col2 = st.columns([3,6])
        with col1:
            st.subheader('**The Learning Gate** - Data Scientist')
            def get_logo():
                img = Image.open('/Users/marcoescobararrazola/Documents/RETO_InferencialStats/data/Logo_del_ITESM.png')
                st.image(img, width=250)
            get_logo()

        with col2:
            st.header('👨🏻‍💻 Reto: Costo Póliza de Seguro (Análisis inferencial)')
            st.subheader('🎯 Objetivo')
            st.markdown('''
            **Al realizar el análisis de las variables clave en un problema a resolver:**
            - Podrás conocer la forma de tomar decisiones de acuerdo con la naturaleza de la variable que estás estudiando, ya sea cuantitativa o categórica, así como el tipo de escala.
            - Seleccionarás las herramientas para visualizar medidas estadísticas como: pruebas de hipótesis de un conjunto de dato bidimensionales para describir el comportamiento de una población y el nivel de dependencia de las variables.
            - Podrás construir un resumen ejecutivo que muestre los comportamientos de las variables importantes en tu análisis.
                        ''')
    
        st.subheader('✍🏻 Introducción:')
        st.write('Comprar un auto involucra saber qué factores influyen en el precio para poder tomar las decisiones más adecuadas y hacer rendir el presupuesto.')
        st.subheader('🏆 Instrucciones')
        st.markdown('''
        **El reto será una continuación del caso visto en la sección de prácticas. Ahora Erick cuenta con una base de datos más completa de 1138 registros, lo cual le permitirá realizar una validación de los resultados obtenidos previamente e identificar otros puntos clave del análisis.**
        - Descarga el archivo pdf llamado Caso Costo de Pólizas, ya que en éste se presentan diversos análisis y estadísticas descriptivas que debes analizar para construir un reporte ejecutivo con un análisis del segmento de mercado de pacientes con Pólizas de Seguro.
        - Descarga los estadísticos que se muestran en el documento Insurance-Reto, para profundizar más en el conocimiento de los datos.
        - Copia, pega y contesta, en un documento de edición de texto, cada uno de los puntos que se solicitan a continuación, basándote en los 2 archivos del punto 1 y 2
                ''')
    
    elif navegador == 'Clasificar variables':
        st.header('📝 Clasificar Variables')
        st.markdown('Dada la lista de variables, clasifícalas en cuantitativas o categóricas. Además de mostrar su escala: nominal, ordinal, intervalo o razón.')
        
        st.subheader('Tabla: Base de datos')
        df = pd.read_excel("/Users/marcoescobararrazola/Documents/RETO_InferencialStats/data/Insurance-Reto.xlsx", sheet_name="Datos Costo Póliza")
        df = df.head(5)
        st.dataframe(df)
        st.subheader('Tabla: Clasificador de variables')
        Clasificador = pd.DataFrame({'Variables':df.columns, 
                             'Cuantitativas':['✅', '❌', '✅', '✅','❌','✅'],
                            'Cualitativas': ['❌', '✅', '❌', '❌', '✅','❌'],
                             'Escala':['Discreta - De razón','Nominal','Continua - De razón','Discreta - De razón','Nominal','Continua - De razón']})
        st.dataframe(Clasificador)
    
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