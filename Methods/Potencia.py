"""
    Método de la Potencia
    Se ingresa una matriz cuadrada A y un vector inicial x0.
    Obtiene el mayor autovalor dominante y su autovector asociado.
"""

import numpy as np
import pandas as pd

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

        # nuevo vector normalizado
        x = y / c

        x_norm = y / -y[0]

        # guardar el valor propio aproximado (c) y vector asociado (normalizado)
        # guardar cada componente del vector como una columna
        # Fila: número de iteración, c, componentes del vector
        c = -c

        fila = [k] + [c] + list(x_norm)
        historial.append(fila)

        # Crear nombres de columna dinámicamente
        cols = ["n", "c"] + [f"x{i+1}" for i in range(len(x_norm))]

        df = pd.DataFrame(historial, columns=cols)


    # Valor propio dominante y vector asociado
    return c, x_norm, df