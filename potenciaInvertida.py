"""
    Método de la Potencia Invertida
    Calcula el autovalor más pequeño de una matriz.
"""

import numpy as np


def metodoPotenciaInvertida(A, tol=1e-6, max_iter=100):
    n = len(A)
    A = A.astype(float)

    # Vector inicial
    x = np.ones(n)
    x = x / np.linalg.norm(x)

    lambda_old = 0

    # Factorización LU para resolver Ax = b cada iteración
    L, U = descomposicionLU(A)

    for k in range(max_iter):

        # Resolver A y = x  →  Ly = x  y luego Ux = y
        y = resolverLU(L, U, x)

        # Normalizar
        x = y / np.linalg.norm(y)

        lambda_new = np.dot(x, np.dot(A, x))

        if abs(lambda_new - lambda_old) < tol:
            break

        lambda_old = lambda_new

    return lambda_new, x, k+1


def descomposicionLU(A):
    """Doolittle simple sin pivoteo."""
    n = len(A)
    L = np.eye(n)
    U = np.zeros((n, n))

    for i in range(n):
        for j in range(i, n):
            U[i, j] = A[i, j] - sum(L[i][k] * U[k][j] for k in range(i))
        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]
    return L, U


def resolverLU(L, U, b):
    """Resuelve Ly=b y Ux=y"""
    n = len(L)
    y = np.zeros(n)

    # Sustitución hacia adelante
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])

    x = np.zeros(n)
    # Sustitución hacia atrás
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return x
