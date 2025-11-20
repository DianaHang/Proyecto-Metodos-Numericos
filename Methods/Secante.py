'''
    Este programa implementa las soluciones que satisfacen 
    las ecuaciones dadas mediante el uso del método de la Secante
'''

import math
import pandas as pd

#Funciones disponibles
def f1(x):
    return (3*x) - (x+2)**2 * math.exp(-x)

def f2(x):
    return math.cos(x) + 2*math.sin(x) + x**2

def f3(x):
    return math.sin(x) - 0.5

#Función para validar inputs numéricos
def leerInput():
    while True:
        for i in range(2):
            #Solicitar inputs muestra
            xStr = input(f"Escriba el valor inicial de la entrada x{i}: ")
            #Validar si se recibe una entrada numérica
            try:
              return float(xStr)
            except ValueError:
              print("Error: La entrada debe ser un número válido.\n")

#Método de la Secante
def metodoSecante(f, x0, x1, n):
    datos = []

    for i in range(1, n+1):

        fx0 = f(x0)
        fx1 = f(x1)

        if fx1 - fx0 == 0:
            raise ZeroDivisionError(
                f"División entre cero en la iteración {i}. No se puede continuar."
            )

         # Fórmula de la secante
        xn = x1 - fx1 * (x1 - x0) / (fx1 - fx0)

        # Evaluar f(xn)
        fxn = f(xn)

        # Guardar datos para DataFrame
        datos.append([i, xn, fxn])

        # Actualizar puntos
        x0, x1 = x1, xn

    df = pd.DataFrame(datos, columns=["n", "xn", "f(xn)"])
    return df, xn