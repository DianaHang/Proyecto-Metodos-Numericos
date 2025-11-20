"""
    Método de la Potencia Inversa:
    En este método se busca el autovalor mínimo (en valor absoluto) de una matriz A.
    Se ingresa una matriz cuadrada A y un vector inicial x0.
    En cada iteración se realiza:
        Ainv y = x
            donde Ainv es la inversa de A
"""
import numpy as np

from Methods.inputsMatriz import mainInputs as ingresarDatos

#Método de la Potencia Inversa
def metodoPotenciaInversa(A, x0, numIter):

    A = A.astype(float)
    n = len(A)

    # Verificar que A sea invertible
    if np.linalg.det(A) == 0:
        raise ValueError("La matriz A NO es invertible, no se puede aplicar potencia inversa.")

    #Convertir x0 a array numpy
    x = np.array(x0, dtype=float)

    # Verificar vector inicial no nulo
    if np.allclose(x, 0):
        raise ValueError("El vector inicial x0 NO puede ser el vector nulo.")

    # Normalizar vector inicial
    x = x / np.linalg.norm(x)

    historial = []

    for k in range(numIter):

        # Resolver Ainv
        y = np.linalg.solve(A, x)

        # Componente dominante
        c = np.max(np.abs(y))

        if c == 0:
            raise ValueError("El método falla: y es el vector nulo.")

        # Nuevo vector normalizado
        x = y / c

        # Autovalor aproximado
        lambda_k = 1 / c

        # Guardar datos de la iteración
        historial.append((lambda_k, x.copy()))

    # Últimas aproximaciones
    lambda_min = historial[-1][0]
    x_final = historial[-1][1]

    return lambda_min, x_final, historial

def mainPotenciaInversa():
    print("*****MÉTODO DE LA POTENCIA INVERSA*****\n")
    A, x0 = ingresarDatos()

    numIter = int(input("\nIngrese el número de iteraciones a calcular: "))

    # Ejecutar método de la potencia inversa
    eigenvalor_min, eigenvector, historial = metodoPotenciaInversa(A, x0, numIter)

    #Mostrar resultados
    print("RESULTADOS DEL MÉTODO DE LA POTENCIA INVERSA\n")

    print("\nValor propio mínimo aproximado:")
    print(f"λ_min ≈ {eigenvalor_min:.8f}\n")

    print(f"Vector propio asociado a {eigenvalor_min}: \n")
    for i, val in enumerate(eigenvector):
        print(f"x{i+1} = {val:.6f}")

    print("Iteraciones:")
    for k, (lambdak, xv) in enumerate(historial):
        print(f"Iteración {k+1}:")
        print(f"  λ ≈ {lambdak:.8f}")
        print(f"  x = {xv}\n")

    print("\nComprobación: \nA·x ≈ λ·x:")
    print(A @ eigenvector)  # Multiplicación matricial A·x

