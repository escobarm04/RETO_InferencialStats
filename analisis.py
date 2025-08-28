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
#Prueba de Normalidad
from scipy.stats import *


# Importamos libreria
df = pd.read_excel("/Users/marcoescobararrazola/Downloads/Insurance-Reto.xlsx", sheet_name="Datos Costo Póliza")

# Realizamos la clasificacion
Clasificador = pd.DataFrame({'Variables':df.columns, 
                             'Cuantitativas':['✅', '❌', '✅', '✅','❌','✅'],
                            'Cualitativas': ['❌', '✅', '❌', '❌', '✅','❌'],
                             'Escala':['Discreta - De razón','Nominal','Continua - De razón','Discreta - De razón','Nominal','Continua - De razón']})

# Calculemos y almacenemos la media, la desviación estándar y el tamaño de la muestra que serán requeridos para la prueba t:
x = round(np.mean(df['Costo Póliza']),2)
s = round(np.std(df['Costo Póliza']),2)
n = len(df)

print(f"Media muestral (x): {x}")
print(f"Desviación estándar muestral (s): {s}")
print(f"Tamaño de la muestra (n): {n}")

#Graficamos QQplot e histograma
def show_fig1():
    fig, ax = plt.subplots(1,2, figsize = (10,6))
    probplot(df['Costo Póliza'], dist="norm", plot=ax[0])
    ax[0].set_title("QQ-Plot de Costo Póliza")
    sns.histplot(df['Costo Póliza'], kde=True, ax = ax[1])
    ax[1].set_title("Histograma de Costo Póliza")
    return fig

def show_fig2():
    # Parámetros
    alpha = 0.05
    gl = n - 1 # Grados de libertad

    # Rango de valores t y PDF
    t_vals = np.linspace(-10, 10, 1000)
    pdf_vals = t.pdf(t_vals, gl) # Distribución t para "gl" grados de libertad

    # Puntos críticos para alfa bilateral derecha
    t_critico_izq = t.ppf(alpha, gl) # Zona de rechazo izquierda ASUMIENDO DISTRIBUCIÓN CON "df" GRADOS DE LIBERTAD

    # Graficar la distribución
    plt.figure(figsize=(10, 6))
    plt.plot(t_vals, pdf_vals, label=f"Distribución t con {gl} grados de libertad", color='blue')

    # Zonas de rechazo izquierda y derecha
    t_rechazo_izq = np.linspace(-5, t_critico_izq, 100) 
    plt.fill_between(t_rechazo_izq, t.pdf(t_rechazo_izq, gl), color='blue', alpha=0.4)

    # Calcular la estadística de esta prueba
    tval = (x-9480)/(s/np.sqrt(n))

    # Y dibujar esta estadística en la distribución anterior
    plt.axvline(tval, color='red', linestyle='--', label=f't observado = {tval:.2f}')

    # Etiquetas
    plt.title('Prueba t: distribución y zonas de rechazo (bilateral)')
    plt.xlabel('Valor t')
    plt.ylabel('Densidad')
    plt.legend()
    plt.grid(True)

    fig = plt.gcf()
    return fig

print('Es evidente que el estadistico de t se encuentra hasta el otro extremos de la zona de rechazo, no se rechaza la hipótesis nula')

Male = df[df['Género'] == 'male']['Indice de masa corporal']
Female = df[df['Género'] == 'female']['Indice de masa corporal']
x_male = round(Male.mean(),2)
s_male = round(Male.std(),2)

x_female = round(Female.mean(),2) 
s_female = round(Female.std(),2)


def show_fig3():
    fig, ax = plt.subplots(2,2, figsize = (10,6))
    probplot(Male, dist="norm", plot=ax[0,0], )
    ax[0,0].set_title("QQ-Plot de IBM en hombres")
    sns.histplot(pd.DataFrame(Male), kde=True, ax = ax[0,1], )
    ax[0,1].set_title("Histograma de IBM en hombres")
    ax[0,1].legend('')
    probplot(Female, dist="norm", plot=ax[1,0])
    ax[1,0].set_title("QQ-Plot de IBM en mujeres")
    sns.histplot(pd.DataFrame(Female), kde=True, ax = ax[1,1])
    ax[1,1].set_title("Histograma de IBM en mujeres")
    ax[1,1].legend('')
    plt.tight_layout()
    return fig

def show_fig4():
    # Parámetros
    alpha = 0.05
    gl = len(Male) + len(Female) - 2 # Grados de libertad

    # Rango de valores t y PDF
    t_vals = np.linspace(-10, 10, 1000)
    pdf_vals = t.pdf(t_vals, gl) # Distribución t para "gl" grados de libertad

    # Puntos críticos para alfa bilateral derecha
    t_critico_izq = t.ppf(alpha, gl) # Zona de rechazo izquierda ASUMIENDO DISTRIBUCIÓN CON "df" GRADOS DE LIBERTAD

    # Graficar la distribución
    plt.figure(figsize=(10, 6))
    plt.plot(t_vals, pdf_vals, label=f"Distribución t con {gl} grados de libertad", color='blue')

    # Zonas de rechazo izquierda y derecha
    t_rechazo_izq = np.linspace(-10, t_critico_izq, 100) 
    plt.fill_between(t_rechazo_izq, t.pdf(t_rechazo_izq, gl), color='blue', alpha=0.4)

    # Calcular la estadística de esta prueba
    tval = (x_female-x_male)/(np.sqrt((s_female)**2/len(Female) + (s_male)**2/len(Male)))

    # Y dibujar esta estadística en la distribución anterior
    plt.axvline(tval, color='black', linestyle='--', label=f't observado = {tval:.2f}')

    # Etiquetas
    plt.title('Prueba t: distribución y zonas de rechazo (bilateral)')
    plt.xlabel('Valor t')
    plt.ylabel('Densidad')
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    return fig
