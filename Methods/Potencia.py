"""
    Método de la Potencia
    Se ingresa una matriz cuadrada A y un vector inicial x0.
    Obtiene el mayor autovalor dominante y su autovector asociado.
"""

import numpy as np

from Methods.inputsMatriz import mainInputs as ingresarDatos

#Método de la Potencia
def metodoPotencia(A, x0, numIter):

    A = A.astype(float)
    n = len(A)

    # Convertir x0 a array numpy
    x = np.array(x0, dtype=float)

    # Verificar que x0 no sea vector nulo
    if np.allclose(x, 0):
        raise ValueError("El vector inicial x0 NO puede ser el vector nulo.")

    historial = []

    for k in range(numIter):
        # y = A x
        y = A @ x

        # componente dominante (valor absoluto máximo)
        c = np.max(np.abs(y))

        if c == 0:
            raise ValueError("El método falla: y es el vector nulo. El método no puede continuar con este vector inicial.")

        # nuevo vector x
        x = y / c

        #Valor propio aproximado
        lambda_k = c

        #Vector propio asociado
        x_k = y / np.abs(y)

        # Guardar datos de la iteración
        historial.append((lambda_k, x_k.copy()))

    return lambda_k, x_k, historial

def mainPotencia():
    print("*****MÉTODO DE LA POTENCIA*****\n")
    A, x0 = ingresarDatos()

    numIter = int(input("\nIngrese el número de iteraciones a calcular: "))

    # Ejecutar método de la potencia
    eigenvalor, eigenvector, historial = metodoPotencia(A, x0, numIter)

    #Mostrar resultados
    print(f"\nEl valor propio dominante es: {eigenvalor}")
    print(f"El vector propio asociado a {eigenvalor} es:\n{eigenvector}")

    #Iteraciones
    print("\n Iteraciones (valor propio, vector propio):")
    for i, (c, x) in enumerate(historial, start=1):
        print(f"Iteración {i-1}: Autovalor = {c}, Autovector = {x}")

    print("\nComprobación Ax = λx: \n")
    print(A @ eigenvector)  # Multiplicación matricial A·x