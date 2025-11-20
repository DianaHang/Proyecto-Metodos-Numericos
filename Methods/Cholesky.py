"""
    Factorización de Cholesky:
    A = L · L^T, con A simétrica y definida positiva.
    Devuelve L, L^T, vector v (Lv=b) y vector x (L^T x = v).
"""
import numpy as np
import pandas as pd

from Methods.inputsMatriz import mainInputs as ingresarDatos

#Método de Cholesky
def cholesky(A, b):
    n = len(A)
    L = np.zeros((n, n))

    # Construir L usando el algoritmo de Cholesky
    for i in range(n):
        for j in range(i + 1):
            suma = sum(L[i][k] * L[j][k] for k in range(j))

            if i == j:
                val = A[i][i] - suma
                if val <= 0:
                    raise ValueError("La matriz NO es definida positiva. "
                                    "A[i][i] - sum <= 0.")
                L[i][j] = np.sqrt(val)
            else:
                if L[j][j] == 0:
                    raise ValueError("La matriz no es apta para Cholesky (tiene ceros en la diagonal).")
                L[i][j] = (A[i][j] - suma) / L[j][j]

    # Sustitución progresiva: L v = b
    v = np.zeros(n)
    for i in range(n):
        v[i] = (b[i] - sum(L[i][k] * v[k] for k in range(i))) / L[i][i]

    # Sustitución regresiva: L^T x = v
    Lt = L.T # Transpuesta de L
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (v[i] - sum(Lt[i][k] * x[k] for k in range(i+1, n))) / Lt[i][i]

    return L, Lt, v, x
