"""
    Método de la Potencia Inversa:
    En este método se busca el autovalor mínimo (en valor absoluto) de una matriz A.
    Se ingresa una matriz cuadrada A y un vector inicial x0.
    En cada iteración se realiza:
        Ainv y = x
            donde Ainv es la inversa de A
"""
import numpy as np

#Método de la Potencia Inversa
def metodoPotenciaInversa(A, x0, numIter):

    A = A.astype(float)
    #Convertir x0 a array numpy
    x = np.array(x0, dtype=float)

    # Verificar vector inicial no nulo
    if np.allclose(x, 0):
        raise ValueError("El vector inicial x0 NO puede ser el vector nulo.")


    # Verificar que A sea invertible
    if np.linalg.det(A) == 0:
        raise ValueError("La matriz A NO es invertible, no se puede aplicar potencia inversa.")


    historial = []

    for k in range(numIter):

        # Resolver A·y = x  →  y = A^{-1} x
        try:
            #linalg.solve ayuda a calcular la inversa automáticamente
            y = np.linalg.solve(A, x)
        except Exception:
            raise ValueError("Error al resolver el sistema A·y = x")

        # Normalización
        c = np.linalg.norm(y)
        

        if c == 0:
            raise ValueError("El método falla: el vector y se volvió nulo.")

        # Siguiente iteración
        x = y / c

        # Cálculo del autovalor aproximado
        # λ ≈ (xᵀ A x) / (xᵀ x)   → Cociente de Rayleigh
        lambda_aprox = (x.T @ A @ x) / (x.T @ x)

        historial.append((lambda_aprox, x.copy()))

    return lambda_aprox, x, historial
