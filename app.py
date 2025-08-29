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
        st.markdown(">**Es evidente que el estadistico de t se encuentra dentro de la zona de rechazo, se rechaza la hipótesis nula y se acepta la alternativa**")
        st.markdown(r"""
                    #### **5) Obtenemos el valor de p a partir del esatdistico de t-student:**
                    - **Estadística t:** -1.77561
                    - **Valor p:** 0.038033
                    - **Tamaño del efecto actualizado:** 0.105255
                    - **Potencia de la prueba actualizada:** 0.551486
                    """)
    elif navegador == 'Ejercicio No. 3':
        st.subheader('📊 Ejercicio No. 3:')
        st.markdown(r"""
                    **Pregunta:** ¿El costo de la póliza incrementa de acuerdo al numero de hijo que tiene el contratante?

                    #### 1) Definimos $H_0$ y $H_1$
                    - $H_0$: Las medias del costo de la póliza en los grupos de contratantes con 0, 1 y 2 hijos son iguales $\mu_0 = \mu_1 = \mu_2$
                    - $H_1$: no todas las medias en el costo de la póliza en los grupos de contratantes con 0, 1, 2 hijos son iguales"

                    #### 2) Definimos población y estadístico:
                    Población normal con sigma desconocido. Dado que sigma es desconocido y tenemos mas de tres grupos de un factor **ANOVA**.
            
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
                    Tamaño mínimo de la muestra por cada grupo: 82.16
                    
                    > **Es decir que: Para cada grupo de hijos debemos recolectar  83 individuos. Esto si queremos tener una potencia de la prueba de 0.9, un tamaño del efecto de 0.4 y un nivel de significancia de 0.05**
                    
                    #### **2) Estimando medidas de tendencia central:**
                    Media de los grupos(costo de la póliza)
                    1) $\mu_0 = 12365.975602 costo de la póliza en el grupo con 0 hijos
                    2) $\mu_1 = 12731.171832 costo de la póliza en el grupo con 1 hijos
                    3) $\mu_2 = 15073.563734costo de la póliza en el grupo con 2 hijos

                    Desviación estándar (costo de la póliza)
                    1) $\sigma_0$ = 12023.29 costo de la póliza en el grupo con 0 hijos
                    2) $\sigma_1$ = 11823.631451 costo de la póliza en el grupo con 1 hijos
                    3) $\sigma_2$ = 12891.368347 costo de la póliza en el grupo con 2 hijos

                    Vemos que la desviación estándar en cada grupo es sumamente grande respecto al promedio.
                    > La idea es aplicar una prueba de ANOVA de un factor (numero de hijos) para determinar si hay diferencias entr eos grupos con número de hijos es diferente en términos del costo de la póliza
                    
                    #### **3) Verificamos normalidad de nuestros datos:**
                    - > Grupo con 0 hijos, Shapiro test: 4.928874820117834e-25 Rechazamos H₀; los datos no son normales. (p < 0.05)
                    - > Grupo con 1 hijo, Shapiro test: 8.852445660276679e-21 Rechazamos H₀; los datos no son normales. (p < 0.05)
                    - > Grupo con 2 hijo, Shapiro test: 4.782895921601787e-17 Rechazamos H₀; los datos no son normales. (p < 0.05)
                    """)
        st.pyplot(show_fig5())
        st.markdown("> **El QQ-plot y el histograma muestra una distribucion no normal de nuestros dato en los tres grupos analizados**")
        st.markdown(r"""
                    #### **4) Prueba de homocedasticiadad: Prueba de Barlett**
                    Prueba de Bartlett para las agrupaciones:
                    p = 0.3109 ✅ No se rechaza H₀ (p>=0.05): homocedasticidad
                    """)
        st.markdown(r"""
                    #### **5) Gráficamos la distribución del estadistico F y valor crítico:**
                    """)
        st.pyplot(show_fig6())
        st.markdown(">**El estadistico de F cae en la zona de rechazo, se rechaza la hipótesis nula y se acepta la hipotesis alternativa: Hay diferencias entre los tres grupos**")
        st.markdown(r"""
                    #### **6) Obtenemos el valor de p a partir del esatdistico de F de ANOVA de un factor:** """)
        st.table(resultados)
    elif navegador == 'Ejercicio No. 4':
        st.subheader('📊 Ejercicio No. 4:')
        st.markdown(r"""
                    **Pregunta:** ¿Determinar si existe relación entre el género del contratante y la cantidad de hijos?

                    #### 1) Definimos $H_0$ y $H_1$
                        - $H_0$: 𝐿𝑎 𝑐𝑎𝑛𝑡𝑖𝑑𝑎𝑑 𝑑𝑒 ℎ𝑖𝑗𝑜𝑠 𝑒𝑠 𝒊𝒏𝒅𝒆𝒑𝒆𝒏𝒅𝒊𝒆𝒏𝒕𝒆 𝑑𝑒 𝑠𝑖 𝑒𝑙 𝑐𝑜𝑛𝑡𝑟𝑎𝑡𝑎𝑛𝑡𝑒 𝑒𝑠 𝑚𝑢𝑗𝑒𝑟 𝑢 ℎ𝑜𝑚𝑏𝑟𝑒
                        - $H_1$: 𝐿𝑎 𝑐𝑎𝑛𝑡𝑖𝑑𝑎𝑑 𝑑𝑒 ℎ𝑖𝑗𝑜𝑠 𝒏𝒐 𝒆𝒔 𝒊𝒏𝒅𝒆𝒑𝒆𝒏𝒅𝒊𝒆𝒏𝒕𝒆 𝑑𝑒 𝑠𝑖 𝑒𝑙 𝑐𝑜𝑛𝑡𝑟𝑎𝑡𝑎𝑛𝑡𝑒 𝑒𝑠 𝑚𝑢𝑗𝑒𝑟 𝑢 ℎ𝑜𝑚𝑏𝑟𝑒

                    #### 2) Definimos población y estadístico:
                    Población con distribución binomial y multinomial. Dado que sigma es desconocido y tenemos dos grupos categoricos (Cantidad de hijos y género),  procedemos a realizar una prueba de Ji-Cuadrada de independencia
            
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
                    #### 1) Tabla de contingencia: Frecuencias esperadas""")
        st.dataframe(expected)
        st.markdown(r"""
                    #### 2) Tabla de contingencia: Frecuencias esperadas""")
        st.dataframe(observed)
        st.markdown(r"""
                    #### 3) Prueba χ² de independencia: distribución y zona de rechazo""")
        st.pyplot(show_fig7())
        st.markdown(">**El estadistico de Chi-Cuadrada NO cae en la zona de rechazo, por lo tanto no se rechaza la hipótesis nula: Es decir, las proporciones de hijos (0,1,2) son iguales en hombres y mujeres**")
        st.markdown(">La probabilidad de tener 0, 1 o 2 hijos es la misma, sin importar si el contratante es hombre o mujer.**")

        st.markdown(r"""
                    #### 4) Estadídistica de Pearson: """)
        st.dataframe(stats.loc[0, :])
    elif navegador == 'Extra: Ejercicio No. 5':
        st.subheader('📊 Extra: Ejercicio No. 5')
        st.markdown(r"""
                    **Pregunta:** ¿Existen cambios (relación) en el precio promedio del costo de la póliza si el contratante es fumador o no es fumador?

                    #### 1) Definimos $H_0$ y $H_1$
                    - $H_0$: el promedio de pago de una poliza es igual entre fumadores y no fumadores $\mu_nf$ = $\mu_f$
                    - $H_1$: el promedio del pago de una poliza es diferente entre fumadores y no fumadores $\mu_nf$ ≠ $\mu_f$

                    #### 2) Definimos población y estadístico:
                    - ✅ Población con distribución normal 
                    - ❌ Sigma poblaciónal conocida 
                    - ✅ Estadistico de prueba: t-student para dos muestras independientes de dos colas (bilateral)

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
                    Tamaño sugerido de cada muestra (n1=n2): 208.59
                    
                    > **Es decir que: Para cada grupo de fumadores o no fumadores debemos recolectar  209 individuos. Esto si queremos tener una potencia de la prueba de 0.9, un tamaño del efecto de 0.4 y un nivel de significancia de 0.05**
                    
                    #### **2) Estimando medidas de tendencia central:**
                    Medidas de los FUMADORES (costo de la póliza)
                    $\mu_f = 32064.37 costo de la póliza en el grupo de fumadores
                    $\sigma_f$ = 11581.73 costo de la póliza en el grupo de fumadores
                    n = 231 individuos fumadores
                    
                    Medidas de los NO FUMADORES (costo de la póliza)
                    $\mu_nf$ = 18195.97 costo de la póliza en el grupo con no fumadores
                    $\sigma_nf$ = 6058.17 costo de la póliza en el grupo con no fumadores
                    n = 907 individuos no fumadores

                    Vemos que la desviación estándar en cada grupo es sumamente grande respecto al promedio.
                    > La idea es aplicar una prueba de t-student para determinar si hay diferencias entre dos categorias del grupo fumadores(si/no) en términos del costo de la póliza
                    
                    #### **3) Verificamos normalidad de nuestros datos:**
                    - > Grupo con fumadores, Shapiro test: 4.265071255617243e-08 Rechazamos H₀; los datos no son normales. (p < 0.05)
                    - > Grupo con no fumadores, Shapiro test: 4.168302639723238e-27 Rechazamos H₀; los datos no son normales. (p < 0.05)
                    """)
        st.pyplot(show_fig8())
        st.markdown("> **El QQ-plot y el histograma muestra una distribucion no normal de nuestros dato en los dos grupos analizados**")
        st.markdown(r"""
                    #### **5) Gráficamos la distribución del estadistico T y valor crítico:**
                    """)
        st.pyplot(show_fig9())
        st.markdown(">**El estadistico de t cae en la zona de rechazo (derecha, 30.29), se rechaza la hipótesis nula y se acepta la hipotesis alternativa: Hay diferencias entre los dos grupos de fumadores y no fumadores**")
        st.markdown(r"""
                    #### **6) Obtenemos el valor de p a partir del esatdistico de F de ANOVA de un factor:** """)
        st.table(resultadost)
    else:
        st.header('✍🏻 REPORTE EJECUTIVO')
        st.subheader("📝 DATASET:")
        st.markdown("""
                    Es importante destacar que la naturaleza del dataset no permite el desarrollo de pruebas de estadística inferencial paramétrica, sino no paramétricas, dado que los datos no muestran una distribución normal en ninguna de las variables analizadas. Seleccionamos la prueba de normalidad de Shapiro-Wilk, ya que contrasta específicamente si los datos siguen una distribución normal a partir de una combinación de ordenamientos y varianzas. Por otra parte, pruebas como Kolmogorov-Smirnov son menos específicas, pues constituyen una prueba general de bondad de ajuste, no limitada únicamente a la normalidad, y pueden aplicarse a cualquier distribución de referencia.
                    Dicho esto, se aplicó la prueba de Shapiro-Wilk y, adicionalmente, se utilizaron herramientas gráficas (Q-Q plot e histogramas), lo que reforzó la evidencia de que los datos no cumplen con el supuesto de normalidad.
                    """)
        st.subheader("1️⃣ Ejercicio No. 1")
        st.markdown(r"""
                Conocemos la media de la población y suponemos una distribución normal. Sin embargo, no conocemos la desviación estándar (σ). Dado que es desconocida, utilizamos el estadístico t de Student unilateral (cola izquierda).
                 Como se observa en el apartado Ejercicio No. 1, la distribución del estadístico t y el valor crítico muestran que nuestro valor de t se posiciona lejos de la zona de rechazo (p =0.05
                α=0.05). Por lo tanto, no se rechaza la hipótesis nula. Es decir, el promedio de pago de una póliza es igual al promedio poblacional; no existen diferencias estadísticamente significativas. Esto se corroboró con el análisis del valor p, donde se obtuvo p > 0.05.
                 """)
        st.subheader("2️⃣ Ejercicio No. 2")
        st.markdown(r"""
                No conocemos la media ni la desviación estándar de la población. En este caso, utilizamos el estadístico t de Student para dos muestras independientes (mujeres vs. hombres).
                Como se observa en el apartado Ejercicio No. 2, la distribución del estadístico t y el valor crítico muestran que nuestro valor de t se encuentra dentro de la zona de rechazo  α = 0.05. 
                Por lo tanto, se rechaza la hipótesis nula y se acepta la hipótesis alternativa. Es decir, la diferencia en el IMC promedio de hombres es estadísticamente mayor que la de mujeres. 
                Esto se corroboró con el análisis del valor p, donde se obtuvo  p < 0.05.
                 """)
        st.subheader("3️⃣ Ejercicio No. 3")
        st.markdown(r"""
                No conocemos la media ni la desviación estándar de la población, pero contamos con más de tres medias de diferentes grupos (0, 1 y 2 hijos). Por lo tanto, utilizamos un ANOVA de un factor.
                Previo a la prueba, se aplicó Shapiro-Wilk en cada grupo, lo que evidenció que no cumplen normalidad. Además, se realizó una prueba de homocedasticidad (Bartlett) para evaluar la igualdad de varianzas entre grupos, obteniéndose p>0.05, lo que confirma homogeneidad de varianzas.
                Como se observa en el apartado Ejercicio No. 3, la distribución del estadístico F y su valor crítico muestran que nuestro valor de F cae en la zona de rechazo (α=0.05). 
                Por lo tanto, se rechaza la hipótesis nula y se acepta la hipótesis alternativa. Es decir, existen diferencias en la media del costo de la póliza en relación con el número de hijos. Esto se corroboró con el análisis del valor p (p<0.05).
                > Nota: Será necesario realizar una prueba post hoc para determinar entre cuáles grupos existen dichas diferencias o si todos los grupos difieren entre sí en el promedio del costo de la póliza.
                 """)
        st.subheader("4️⃣ Ejercicio No. 4")
        st.markdown(r"""
                La población se modela con distribución binomial/multinomial. Dado que σ es desconocida y trabajamos con dos variables categóricas (género y cantidad de hijos), se aplicó la prueba de Ji-Cuadrada de independencia (Pearson).
                Como se observa en el apartado Ejercicio No. 4, el valor del estadístico χ2=0.210 χ2=0.210 se posiciona fuera de la zona de rechazo (α=0.0). Por lo tanto, no se rechaza la hipótesis nula. En otras palabras, las proporciones de hijos (0, 1 y 2) 
                son iguales en hombres y mujeres; la probabilidad de tener cierta cantidad de hijos es independiente del género del contratante. Esto se corroboró con el valor p obtenido (p>0.05).
                 """)
        st.subheader("5️⃣ Ejercicio No. 5")
        st.markdown(r"""
                Población con distribución normal, sin conocer. Dado que la desviación estándar poblacional es desconocida y tenemos dos grupos (fumadores y no fumadores), se utilizó la prueba t de Student para dos muestras independientes, bilateral (dos colas).
                Como se observa en el apartado Ejercicio No. 5, el valor del estadístico t (30.29) cae dentro de la zona de rechazo (α = 0.05). En consecuencia, se rechaza la hipótesis nula y se acepta la hipótesis alternativa. Es decir, existen diferencias 
                significativas entre fumadores y no fumadores en el promedio de la variable analizada. Esto se corroboró con el análisis del valor p (p<0.05).
                 """)

main()
