import sys
import os

ruta_actual = os.path.dirname(os.path.abspath(__file__))          # /GraphicInterface
ruta_proyecto = os.path.dirname(ruta_actual)                      # /ProyectoFinal

if ruta_proyecto not in sys.path:
    sys.path.insert(0, ruta_proyecto)

"""##################################################
"""

import tkinter as tk
from tkinter import messagebox
import numpy as np
from Methods.GaussSeidel import gaussSeidel
from Methods.inputsMatriz import mainInputs, diagonalDominante


def ventanaGaussSeidel():
    sub = tk.Toplevel()
    sub.title("Método de Gauss-Seidel")
    sub.geometry("420x450")

    tk.Label(sub, text="Método de Gauss - Seidel",
             font=("Arial", 16, "bold")).pack(pady=10)

    # Entrada número de iteraciones
    tk.Label(sub, text="Número de iteraciones:").pack()
    entrada_iter = tk.Entry(sub, width=10)
    entrada_iter.insert(0, "10")
    entrada_iter.pack()

    resultado = tk.Label(sub, text="", wraplength=380, justify="left")
    resultado.pack(pady=10)

    def ejecutar():
        try:
            numIter = int(entrada_iter.get()) + 1

            # Obtener A y b
            A, b = mainInputs()

            # Intentar reordenar
            ADom, bDom = diagonalDominante(A, b)
            if ADom is None:
                ADom = A
                bDom = b

            # Ejecutar Gauss-Seidel
            solucion, dfGS = gaussSeidel(ADom, bDom, numIter)

            salida = "Resultados por iteración:\n\n"
            salida += dfGS.to_string(index=False)
            salida += "\n\nSolución aproximada:\n" + str(solucion)

            resultado.config(text=salida)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(sub, text="Calcular", command=ejecutar).pack(pady=5)
    tk.Button(sub, text="Cerrar", command=sub.destroy).pack(pady=5)
    sub.mainloop() # Mantener la ventana abierta