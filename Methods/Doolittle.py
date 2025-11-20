"""
    Factorización LU por el método de Doolittle (L con diagonal unitaria).
    Devuelve L, U, vector v (Ly=b) y solución x (Ux=v).
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from Methods.inputsMatriz import mainInputs as ingresarDatos
   
#Método de Doolittle
def doolittle(A, b):
    A = A.astype(float)
    n = len(A)

    #Incializar matrices L y U en ceros
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    # Construcción de L y U
    for i in range(n):
        # Calcular fila de U
        for j in range(i, n):
            suma = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - suma

        # Calcular columna de L
        L[i][i] = 1  # diagonal unitaria
        for j in range(i+1, n):
            suma = sum(L[j][k] * U[k][i] for k in range(i))
            if U[i][i] == 0:
                raise ValueError("El método falla: pivote cero.")
            L[j][i] = (A[j][i] - suma) / U[i][i]

    # Sustitución progresiva (Ly = b)
    v = np.zeros(n)
    for i in range(n):
        v[i] = b[i] - sum(L[i][j] * v[j] for j in range(i))

    # Sustitución regresiva (Ux = v)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        if U[i][i] == 0:
            raise ValueError("El método falla: U tienes ceros en la diagonal.")
        #Vector solución
        x[i] = (v[i] - sum(U[i][j] * x[j] for j in range(i+1, n))) / U[i][i]

    return L, U, v, x

def mainDoolittle():
    print("*****MÉTODO DE DOOLITTLE*****\n")
    A, b = ingresarDatos()
    
    try:
        L, U, v, x = doolittle(A, b)
        
        print("\nMatriz L:")
        print(L)
        print("\nMatriz U:")
        print(U)
        print("\n (Lv = b): \nSustitución progresiva para v: ")
        print("\nVector v= ")
        v = np.transpose(v)
        print(v)
        print("\n (Ux = v): \nSustitución regresiva para x: ")
        print("\nSolución x= ")
        print(x)
        
    except ValueError as e:
        print("Hubo un error inesperado: \n", e)