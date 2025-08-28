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
from analisis import *

st.set_page_config(page_title='Reto | Costo Póliza de Seguro',
                   page_icon = '🪲', 
                   layout= 'wide', 
                   initial_sidebar_state= 'collapsed')

def main():
    menu = ['Instrucciones', 
            'Clasificar variables', 
            'Ejercicio No. 1', 
            'Ejercicio No. 2',
            'Ejercicio No. 3',
            'Ejercicio No. 4',
            'Extra: Ejercicio No. 5',
            'Resumen ejecutivo',]
    navegador = st.sidebar.selectbox('📊 NAVEGADOR:', menu, )

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
        st.subheader('📊 Ejercicio No. 1:')
        st.markdown(r"""
                    **Pregunta:** ¿El monto promedio que una persona paga por la póliza de seguros es estadísticamente menor que los $9{,}480 dólares$ que se pagan en promedio en la población?

                    #### 1) Definimos $H_0$ y $H_1$
                    - $H_0$: el promedio de pago de una póliza es igual al promedio de 9480 dólares $\rightarrow \bar{x} = \mu$
                    - $H_1$: el promedio de una póliza es **menor** que el promedio de 9480 dólares $\rightarrow \bar{x} < \mu$

                    #### 2) Definimos población y estadístico:
                    Población normal con sigma desconocido. Dado que sigma es desconocido utilizamos estadístico **t-student**.

                    1) $\mu = 9480$ dólares (Población)  
                    2) $\bar{x} = 13040.97$ dólares (Muestra)

                    #### 3) Definimos $\alpha$:
                    $\alpha = 0.05$

                    **Normal Distribution Calculator:** https://www.infrrr.com/distributions/normal-distributions

                    #### 4) Definimos la potencia de la prueba $(1-\beta)$ y el tamaño de la muestra $(n)$:
                    - 0.2: efecto "pequeño"  
                    - 0.5: efecto "mediano"  
                    - 0.8: efecto "grande"
                    """)
        st.subheader('Desarrollo:')
        st.markdown(r"""
                    #### **1) Estimando tamaño de muestra:**
                    Tamaño de la muestra: **25.20**. Es decir que para un efecto de 0.6 (-0.6 al ser unilatera izquierda) y una potencia de la prueba de 0.9 requerimos al menos 25.2
                    Es importante destacar que nuestro tamaño de muestra supera fácilmente esto, con una n = 1138.
                    
                    #### **2) Estimando medidas de tendencia central:**
                    - Media muestral (x): 13040.97
                    - Desviación estándar muestral (s): 12185.97
                    - Tamaño de la muestra (n): 1138
                    
                    #### **3) Verificamos normalidad de nuestros datos:**
                    - Shapiro tests en la población muestral: 2.0425435393207283e-34 No cumple con una distribución normal (p < 0.05)
                    > **Es importante destacar que nuestros datos no siguen una distribución normal: 
                    Nuestro valor de p es menor a 0.05 y por lo tanto se rechaza la hipótesis nula que indica distribución normal**
                    """)
        st.pyplot(show_fig1())
        st.markdown("> **El QQ-plot y el histograma muestra una distribucion no normal de nuestros datos**")
        st.markdown(r"""
                    #### **4) Gráficamos la distribución del estadistico t y valor crítico:**
                    """)
        st.pyplot(show_fig2())
        st.markdown(">**Es evidente que el estadistico de t se encuentra hasta el otro extremos de la zona de rechazo, no se rechaza la hipótesis nula**")
        st.markdown(r"""
                    #### **5) Obtenemos el valor de p a partir del esatdistico de t-student:**
                    - Estadística t: 9.85
                    - Valor p: 1.0
                    - Tamaño del efecto actualizado: 0.292
                    - Potencia de la prueba actualizada: 1.5721415800669329e-30 (Practicamente 0)
                    """)
   
    elif navegador == 'Ejercicio No. 2':
        st.subheader('📊 Ejercicio No. 2:')
        st.markdown(r"""
                Pregunta: ¿Las mujeres presentan un promedio de IBM significativamente menor que el promedio de IBM de los hombres?

                #### 1) Definimos $H_0$ y $H_1$
                - $H_0$: la diferencia en el IBM promedio de hombres y mujeres no es diferente $\mu_F - \mu_M = 0$
                - $H_1$: la diferencia en el IBM promedio de hombres es mayor al IBM promedio de mujeres  $\mu_F - \mu_M < 0$
                #### 2) Definimos población y estadístico:
                No conocemos la media y sigma de la población. Por lo tanto, utilizamos el estadístico **t-student** para dos muestras independientes. Una muestra Female y otras muestra Male

                #### 3) Definimos $\alpha$:
                $\alpha$: 0.05

                Nota: Herramienta interesante en para evaluar algún estadistico. 
                **Normal Distribution Calculator:** https://www.infrrr.com/distributions/normal-distributions
                #### 4) Definimos la potencia de la prueba $(1-\beta)$ y el tamaño de la muestra $(n)$:
                Comencemos definiendo el tamaño del efecto ($d$):
                - 0.2: efecto "pequeño"
                - 0.5: efecto "mediano"
                - 0.8: efecto "grande"
                    """)
        st.subheader('Desarrollo:')
        st.markdown(r"""
                    #### **1) Estimando tamaño de muestra:**
                    Tamaño sugerido de cada muestra (n1=n2): 69.1978218601091
                    
                    > **Es decir que: Para cada género debemos recolectar el IBM promedio de al menos 70 personas. Esto si queremos tener una potencia de la prueba de 0.9, un tamaño del efecto de 0.8 y un nivel de significancia de 0.05**
                    
                    #### **2) Estimando medidas de tendencia central:**
                    1) $\mu_m$ = 30.98
                    2) $\sigma_m$ = 6.24
                    3) $\mu_f$ = 30.34
                    4) $\sigma_f$ = 6.06

                    Vemos que el IBM promedio de los hombres es ligeramente superior al IBM de mujeres (30.98 IBM en hombres vs. 30.34 IBM en mujeres).
                    > La idea es aplicar el t-test de muestras independientes para determinar si un valor menor de IBM en mujeres es resultado de que las mujeres son más sanas que los hombres o es producto del azar.
                    
                    #### **3) Verificamos normalidad de nuestros datos:**
                    - > 👨🏻‍🦰 Shapiro test en Hombres: 0.008043844042743392, Rechazamos H₀; los datos no son normales. (p < 0.05)
                    - > 🙋🏼‍♀️ Shapiro test en Mujeres: 0.010867842574999502 Rechazamos H₀; los datos no son normales. (p < 0.05)
                    """)
        st.pyplot(show_fig3())
        st.markdown("> **El QQ-plot y el histograma muestra una distribucion no normal de nuestros datos**")
        st.markdown(r"""
                    #### **4) Gráficamos la distribución del estadistico t y valor crítico:**
                    """)
        st.pyplot(show_fig4())
        st.markdown(">**Es evidente que el estadistico de t se encuentra hasta el otro extremos de la zona de rechazo, no se rechaza la hipótesis nula**")
        st.markdown(r"""
                    #### **5) Obtenemos el valor de p a partir del esatdistico de t-student:**
                    - **Estadística t:** -1.77561
                    - **Valor p:** 0.038033
                    - **Tamaño del efecto actualizado:** 0.105255
                    - **Potencia de la prueba actualizada:** 0.551486
                    """)
    elif navegador == 'Ejercicio No. 3':
        pass
    elif navegador == 'Ejercicio No. 4':
        pass
    elif navegador == 'Extra: Ejercicio No. 5':
        pass
    else:
        pass

main()