"""
    Método de la Potencia
    Obtiene el mayor autovalor dominante y su autovector asociado.
"""

import numpy as np


def metodoPotencia(A, tol=1e-6, max_iter=100):
    n = len(A)
    A = A.astype(float)

    # Vector inicial
    x = np.ones(n)
    x = x / np.linalg.norm(x)

    lambda_old = 0

    for k in range(max_iter):
        # Multiplicación
        y = np.dot(A, x)

        # Normalizar
        x = y / np.linalg.norm(y)

        # Aproximación del autovalor (cociente de Rayleigh)
        lambda_new = np.dot(x, np.dot(A, x))

        # Verificar convergencia
        if abs(lambda_new - lambda_old) < tol:
            break

        lambda_old = lambda_new

    return lambda_new, x, k+1


def mainPotencia():
    print("***** MÉTODO DE LA POTENCIA *****\n")

    # Ejemplo temporal
    A = np.array([[4, 1],
                  [2, 3]], float)

    lambda_dom, vector, iters = metodoPotencia(A)
    print(f"Autovalor dominante = {lambda_dom}")
    print(f"Autovector:\n{vector}")