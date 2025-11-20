'''
    Este programa consiste en calcular el vector
    solución que resuelve cualquier sistema de 
    ecuaciones lineales mediante el Método de Jacobi,
    el cual requiere que su matriz de coeficientes
    tenga inversa y que su diagonal sea dominante.
'''
import numpy as np
import pandas as pd

from Methods.inputsMatriz import mainInputs as ingresarDatos
from Methods.inputsMatriz import diagonalDominante as reacomodarFilas
   
#Método de Jacobi
def jacobi(A, b, numIter):
    n  = len(A)
    #Inicializar vector inicial x0= (0,0,..., n) y el siguiente
    x = np.zeros(n)
    xn = np.zeros(n)
    
    # Lista para crear DataFrame
    listaIteraciones = []
    
    #Iteraciones para obtener x1, x2, ..., xn
    for i in range(1, numIter):
        for j in range(n):
            despeje = 0
            for k in range(n):
                #Despeje de acuerdo al número de ecuación y número de variable
                if j != k:
                    despeje += A[j,k] * x[k]
            xn[j] = (b[j].item() - despeje) / A[j, j].item()
            
        # Registrar iteración para DataFrame
        nuevaFila = {"n": i}
        for indx, valor in enumerate(xn):
            nuevaFila[f"x{indx+1}"] = valor
        listaIteraciones.append(nuevaFila)
        
        x = xn.copy()
        
    df = pd.DataFrame(listaIteraciones)
    return x, df

