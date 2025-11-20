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

        # Resolver A·y = x  →  y = A^{-1} x sin invertir
        try:
            y = np.linalg.solve(A, x)
        except Exception:
            raise ValueError("Error al resolver el sistema A·y = x")

        # Componente dominante (autovalor aproximado inverso)
        c = np.max(np.abs(y))

        if c == 0:
            raise ValueError("El método falla: el vector y se volvió nulo.")

        # Vector normalizado para siguiente iteración
        x_normalizado = y / c

        # Vector propio escalado al estilo clásico
        # Último componente igual a 1 (si posible)
        if np.abs(y[-1]) > 1e-12:
            x_escalado = y / y[-1]
        else:
            idx = np.argmax(np.abs(y))
            x_escalado = y / y[idx]

        # Para siguiente iteración
        x = x_normalizado.copy()

        historial.append((1/c, x_normalizado.copy(), x_escalado.copy()))

    # Últimos valores
    eigenvalor_inverso = 1/c
    eigenvector_normalizado = x_normalizado.copy()
    eigenvector_escalado = x_escalado.copy()

    return eigenvalor_inverso, eigenvector_normalizado, eigenvector_escalado, historial
