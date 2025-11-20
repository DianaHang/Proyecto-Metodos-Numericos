'''
    Este programa implementa las soluciones que satisfacen 
    las ecuaciones dadas mediante el uso del método de Newton 
'''
import math
import pandas as pd
import matplotlib.pyplot as plt

#Funciones muestra y sus derivadas
def f1(x):
    return (3*x) - (x+2)**2 * math.exp(-x)

def df1(x):
    return 3 - 2*(x+2)*math.exp(-x) + (x+2)**2 * math.exp(-x)
    
def f2(x):
    return math.cos(x) + 2 * math.sin(x) + x**2

def df2(x):
    return - math.sin(x) + 2 * math.cos(x) + 2*x

def f3(x):
    return math.sin(x) - 0.5

def df3(x):
    return math.cos(x)

#Método de Newton
def metodoNewton(f, df, x0, n):
    # Listas para crear un Data Drame (df)
    iteraciones = []
    xList = []
    fList = []
    derivList = []
    
    #Valor inicial
    xn = x0
    
    #Realizar iteraciones con método de Newton
    for i in range(n):
        fx = f(xn)
        dfx = df(xn)
    
        #Validar no división por cero
        if dfx == 0:
            raise ValueError("La derivada es cero. El método no puede continuar.")
    
        #Almacenar datos en las listas del DF
        iteraciones.append(i+1)
        xList.append(xn)
        fList.append(fx)
        derivList.append(dfx)

        #Actualizar valor de xn
        xn = xn - (fx / dfx)
    
    #Creacion del Data Frame
    df_res = pd.DataFrame({
        "n": iteraciones,
        "xn": xList,
        "f(xn)": fList,
        "f'(xn)": derivList
        })
    
    #Mostrar el Data Frame hasta el último valor
    return df_res, xn
