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

#ANOVA
media = df.groupby(by = 'Cantidad de hijos')['Costo Póliza'].mean()
std = df.groupby(by = 'Cantidad de hijos')['Costo Póliza'].std()

def show_fig5():
    fig, ax = plt.subplots(3, 2, figsize = (6, 10))
    probplot(df.loc[df['Cantidad de hijos']== 0,'Costo Póliza'], dist="norm", plot=ax[0,0], )
    ax[0,0].set_title("QQ-Plot de grupo de 0 hijos")
    sns.histplot(df.loc[df['Cantidad de hijos']== 0,'Costo Póliza'], kde=True, ax = ax[0,1], )
    ax[0,1].set_title("Histograma de grupo de 0 hijos")

    probplot(df.loc[df['Cantidad de hijos']== 1,'Costo Póliza'], dist="norm", plot=ax[1,0], )
    ax[1,0].set_title("QQ-Plot de grupo de 1 hijo")
    sns.histplot(df.loc[df['Cantidad de hijos']== 1,'Costo Póliza'], kde=True, ax = ax[1,1], )
    ax[1,1].set_title("Histograma de grupo de 1 hijo")

    probplot(df.loc[df['Cantidad de hijos']== 2,'Costo Póliza'], dist="norm", plot=ax[2,0], )
    ax[2,0].set_title("QQ-Plot de grupo de 2 hijos")
    sns.histplot(df.loc[df['Cantidad de hijos']== 2,'Costo Póliza'], kde=True, ax = ax[2,1], )
    ax[2,1].set_title("Histograma de grupo de 2 hijos")
    plt.tight_layout()

    return fig

#PRUEBA DE HOMOCEDASTICIDAD
niveles = df['Cantidad de hijos'].unique() # 0, 1, 2 hijos

# Extraer los grupos como arreglos de NumPy
grupos = []
for nivel in niveles:
    grupo = df.loc[df['Cantidad de hijos']== nivel,'Costo Póliza'].to_numpy()
    grupos.append(grupo)

# Y apliquemos la prueba de Bartlett
B, pb = bartlett(*grupos)

# Imprimir resultados
print(f"Prueba de Bartlett para las agrupaciones:")
print(f"  p = {pb:.4f} {'❌ Rechazar H₀ (p<0.05): heterocedasticidad' if pb < 0.05 else '✅ No se rechaza H₀ (p>=0.05): homocedasticidad'}\n")

#GRAFICA DE DISTIRBUCION F
def show_fig6():
    # Grados de libertad y valor de f
    dof_inter = resultados.loc[0,'DF']
    dof_intra = resultados.loc[1,'DF']
    fval = resultados.loc[0,'F']
    alpha = 0.05

    # Distribución F para los "dof / Grados de libertad" obtenidos
    f_vals = np.linspace(0, 7, 1000) # Recordemos que F SIEMPRE es positivo
    pdf_vals = f.pdf(f_vals, dof_inter, dof_intra) # Distribución f

    # Punto crítico para alfa
    f_critico_der = f.ppf(1-alpha, dof_inter, dof_intra) # Recordemos que ANOVA SIEMPRE será prueba unilateral derecha

    # Graficar la distribución
    plt.figure(figsize=(15, 6))
    plt.plot(f_vals, pdf_vals, label=f"Distribución f con {int(dof_inter)} y {int(dof_intra)} grados de libertad", color='blue')

    # Zona de rechazo derecha
    f_rechazo_der = np.linspace(f_critico_der, 7, 100) # Irá desde f_critico_der hasta 20, 100 datos
    plt.fill_between(f_rechazo_der, f.pdf(f_rechazo_der, dof_inter, dof_intra), color='blue', alpha=0.4)

    # Dibujar estadística f en la distribución anterior
    plt.axvline(fval, color='red', linestyle='--', label=f'F observado = {fval:.2f}')

    # Etiquetas
    plt.title('Prueba ANOVA de 1 factor: distribución y zona de rechazo')
    plt.xlabel('Valor F')
    plt.ylabel('Densidad')
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    return fig

datos = df[['Cantidad de hijos', 'Costo Póliza']]

resultados = pg.anova(
    data = datos, # El dataset
    dv = 'Costo Póliza', # Observaciones (variable numérica)
    between = 'Cantidad de hijos', # Columna con el factor
    detailed = True, # Entregar resultados detallados
    effsize = 'n2', # Calcular el tamaño del efecto como eta cuadrado
)
resultados

#PRUEBA DE CHI CUADRADA
# Asegurar que las variables sean categóricas
df['Género'] = df['Género'].astype('category')
df['Cantidad de hijos'] = df['Cantidad de hijos'].astype('category')

# Prueba chi-cuadrada de independencia
expected, observed, stats = pg.chi2_independence(df, x='Género', y='Cantidad de hijos')

print("Tabla de frecuencias esperadas:\n")
expected = pd.DataFrame(expected)
print(expected)
print("\nTabla de frecuencias observadas:\n")
observed = pd.DataFrame(observed)
print(observed)
print("\nResultados de pearson:\n")
stats = pd.DataFrame(stats)


def show_fig7():
    # Parámetros de tu prueba chi-cuadrada
    dof = 2                # tabla 2×3: (2−1)(3−1)=2
    chi2_obs = 0.210443    
    alpha = 0.05           


    x_max = chi2.ppf(0.999, dof)
    x = np.linspace(0, x_max, 1000)
    y = chi2.pdf(x, dof)
    chi2_crit = chi2.ppf(1 - alpha, dof)

    plt.figure(figsize=(12, 5))
    plt.plot(x, y, label=f"χ² con {dof} gl")
    x_rechazo = np.linspace(chi2_crit, x_max, 300)
    plt.fill_between(x_rechazo, chi2.pdf(x_rechazo, dof), alpha=0.3, label=f"Zona de rechazo (α={alpha})")
    plt.axvline(chi2_obs, linestyle='--', color = 'red',  label=f"χ² observado = {chi2_obs:.3f}")
    plt.title("Prueba χ² de independencia: distribución y zona de rechazo")
    plt.xlabel("Valor χ²")
    plt.ylabel("Densidad")
    plt.legend()
    plt.grid(True)
    fig = plt.gcf()
    return fig

#ULTIMO EJERCICIO
fumador = df[df['Fumador'] == 'yes']['Costo Póliza']
no_fumador = df[df['Fumador']== 'no']['Costo Póliza']

x_f = fumador.mean()
s_f = fumador.std()
n_f = len(fumador) 

x_nf = no_fumador.mean()
s_nf = no_fumador.std()
n_nf = len(no_fumador) 


#Porbamos normalidad
def show_fig8():
    fig, ax = plt.subplots(2, 2, figsize = (12, 6))
    probplot(df.loc[df['Fumador']== 'yes','Costo Póliza'], dist="norm", plot=ax[0,0], )
    ax[0,0].set_title("QQ-Plot de grupo de fumadores")
    sns.histplot(df.loc[df['Fumador']== 'yes','Costo Póliza'], kde=True, ax = ax[0,1], )
    ax[0,1].set_title("Histograma de fumadores")

    probplot(df.loc[df['Fumador']== 'no','Costo Póliza'], dist="norm", plot=ax[1,0], )
    ax[1,0].set_title("QQ-Plot de grupo de no fumadores")
    sns.histplot(df.loc[df['Fumador']== 'no','Costo Póliza'], kde=True, ax = ax[1,1], )
    ax[1,1].set_title("Histograma de grupo de no fumadores")
    plt.tight_layout()
    return fig

def show_fig9():
    # Parámetros
    alpha = 0.05
    gl = n_f + n_nf - 2 # Grados de libertad

    # Rango de valores t y PDF
    t_vals = np.linspace(-25, 25, 1000)
    pdf_vals = t.pdf(t_vals, gl) # Distribución t para "gl" grados de libertad

    # Puntos críticos para alfa bilateral derecha
    t_critico_izq = t.ppf(alpha/2, gl) # Zona de rechazo izquierda ASUMIENDO DISTRIBUCIÓN CON "df" GRADOS DE LIBERTAD
    t_critico_der = t.ppf(1-alpha/2, gl)
    # Graficar la distribución
    plt.figure(figsize=(10, 6))
    plt.plot(t_vals, pdf_vals, label=f"Distribución t con {gl} grados de libertad", color='blue')

    # Zonas de rechazo izquierda y derecha
    t_rechazo_izq = np.linspace(-25, t_critico_izq, 100) 
    plt.fill_between(t_rechazo_izq, t.pdf(t_rechazo_izq, gl), color='blue', alpha=0.4)
    t_rechazo_der = np.linspace(30, t_critico_der, 100) 
    plt.fill_between(t_rechazo_der, t.pdf(t_rechazo_der, gl), color='blue', alpha=0.4)

    # Calcular la estadística de esta prueba
    tval = (x_f-x_nf)/(np.sqrt((s_f)**2/n_f + (s_nf)**2/n_nf))

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

resultadost = pg.ttest(
    x = fumador.values,
    y = no_fumador.values, # El segundo arreglo es usualmente el de referencia
    paired = False, # Porque las muestras son independientes
    alternative = 'two-sided', # Nos interesa ver si hubo incremento de la media de B con respecto a A
)
resultadost