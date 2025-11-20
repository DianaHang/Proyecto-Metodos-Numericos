'''
    Este programa consiste en calcular el vector
    solución que resuelve cualquier sistema de 
    ecuaciones lineales mediante el Método de Gauss - Seidel,
    el cual requiere que su matriz de coeficientes
    tenga inversa y que su diagonal sea dominante.
    Tiene un ligero cambio en el cálculo de las incógnitas, 
    en comparación con el método de Jacobi.
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from Methods.inputsMatriz import mainInputs as ingresarDatos
from Methods.inputsMatriz import diagonalDominante as reacomodarFilas
   
#Método de Gauss - Seidel
def gaussSeidel(A, b, numIter):
    n  = len(A)
    #Inicializar vector inicial x0= (0,0,..., n)
    x = np.zeros(n)
    
    # Lista para crear DataFrame
    listaIteraciones = []
    
    #Iteraciones para obtener x1, x2, ..., xn
    for i in range(1, numIter):
        for j in range(n):
            despeje = 0
            for k in range(n):
                #Despeje de acuerdo a los nuevos valores calculados
                if j != k:
                    despeje += A[j,k] * x[k]
                    
            #Actualizar cálculo de nuevos valores para las incógnitas
            x[j] = (b[j].item() - despeje) / A[j, j].item()
            
        # Registrar iteración para DataFrame
        nuevaFila = {"n": i}
        for indx, valor in enumerate(x):
            nuevaFila[f"x{indx+1}"] = valor
        listaIteraciones.append(nuevaFila)
        
    df = pd.DataFrame(listaIteraciones)
    return x, df
