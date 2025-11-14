'''
    Este programa consiste en calcular el vector
    solución que resuelve cualquier sistema de 
    ecuaciones lineales mediante el Método de Jacobi,
    el cual requiere que su matriz de coeficientes
    tenga inversa y que su diagonal sea dominante.
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from inputsMatriz import main as ingresarDatos
from inputsMatriz import diagonalDominante as reacomodarFilas
   
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
            nuevaFila[f"x{indx+1}_n"] = valor
        listaIteraciones.append(nuevaFila)
        
        x = xn.copy()
        
    df = pd.DataFrame(listaIteraciones)
    return x, df

def main():
    print("*****MÉTODO DE JACOBI*****\n")
    A, b = ingresarDatos()
    
    #Reacomodar filas si es necesario
    ADom, bDom = reacomodarFilas(A, b)
    
    if ADom is None:
        print("\nLa matriz no pudo reacomodarse para ser diagonal dominante.")
        print("\nIMPORTANTE: Este método podría no converger.")
        ADom = A
        bDom = b
    else: print("\nSe ha reacomodado la matriz para ser diagonal dominante.\nEs posible continuar.")
    
    numIter = int(input("\nIngrese el número de iteraciones a calcular: ")) + 1
    
    solucion, dfJacobi = jacobi(ADom, bDom, numIter)
    print(dfJacobi)
    
    solucion = np.transpose([solucion])
    
    print(f"\nLa solución aproximada para el sistema asociado a la matriz \n A = \n{A} \n es: x = ")
    print(solucion)
    
    # Gráfica para mostrar convergencia del método
    n = dfJacobi["n"]
    
    plt.figure(figsize=(8,5))
    for col in dfJacobi.columns[1:]:  # Omitir columna de iteraciones
        plt.plot(n, dfJacobi[col], marker="*", label=col, linestyle= "-", color = 'green')

    plt.title("Convergencia del Método de Jacobi")
    plt.xlabel("Iteración n")
    plt.ylabel("Valor aproximado de x")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    main()