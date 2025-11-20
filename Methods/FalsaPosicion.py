'''
    Este programa implementa las soluciones que satisfacen 
    las ecuaciones dadas mediante el uso del método de Falsa posición
'''
import math
import pandas as pd

#Funciones a trabajar
def f1(x):
    return (3*x) - (x+2)**2 * math.exp(-x)

def f2(x):
    return math.cos(x) + 2*math.sin(x) + x**2

def f3(x):
    return math.sin(x) - 0.5


def leerInputs(): #Entradas para el usuario
    while True:
        aStr = input("Escriba el valor inicial del intervalo a: ")
        bStr = input("Escriba el valor inicial del intervalo b: ")

        #Validar si se reciben entradas numéricas
        try:
          a = float(aStr)
          b = float(bStr)
          if f1(a) * f1(b) >= 0: #validación de signos.
              print("\nIMPORTANTE: Si f(a) y f(b) tienen signos iguales, no procede el método; brinde otros valores.\n")
          else:
              return a, b

        except ValueError:
          print("ERROR: INGRESE ENTRADAS VÁLIDAS.\n")
          
#Método de Falsa Posición
def metodoFalsaPosicion(f, a, b, n):
    if f(a) * f(b) > 0:
        raise ValueError("El intervalo no cumple f(a)*f(b) < 0. No se garantiza raíz.")

    datos = []

    for i in range(1, n+1):

        fa = f(a)
        fb = f(b)

        # Punto por Falsa Posición
        c = b - fb * (b - a) / (fb - fa)
        fc = f(c)

        # Guardar en DataFrame
        datos.append([i, a, b, c, fa, fb, fc])

        # Actualizar intervalo
        if fa * fc < 0:
            b = c
        else:
            a = c

    df = pd.DataFrame(datos, columns=["n", "a", "b", "c", "f(a)", "f(b)", "f(c)"])

    return df, c
