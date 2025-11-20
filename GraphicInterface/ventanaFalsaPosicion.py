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
import math
from Methods.FalsaPosicion import metodoFalsaPosicion


def ventanaFalsaPosicion():
    sub = tk.Toplevel()
    sub.title("Método de Falsa Posición")
    sub.geometry("400x400")

    tk.Label(sub, text="Método de Falsa Posición",
             font=("Arial", 16, "bold")).pack(pady=10)

    ecuaciones = {
        "1. x³ - x - 2": "x**3 - x - 2",
        "2. eˣ - 3x": "math.exp(x) - 3*x",
        "3. sin(x) - 0.5": "math.sin(x) - 0.5"
    }

    opcion_var = tk.StringVar(sub, value=list(ecuaciones)[0])

    tk.Label(sub, text="Selecciona una ecuación:").pack()
    tk.OptionMenu(sub, opcion_var, *ecuaciones).pack()

    entradas = {}
    for label in ["a", "b", "tol", "iter"]:
        tk.Label(sub, text=label).pack()
        e = tk.Entry(sub, width=10)
        e.pack()
        entradas[label] = e

    resultado = tk.Label(sub, text="", wraplength=350)
    resultado.pack(pady=10)

    def ejecutar():
        try:
            fx = ecuaciones[opcion_var.get()]
            salida = metodoFalsaPosicion(
                fx,
                float(entradas["a"].get()),
                float(entradas["b"].get()),
                float(entradas["tol"].get()),
                int(entradas["iter"].get())
            )
            resultado.config(text=salida)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(sub, text="Calcular", command=ejecutar).pack(pady=5)
    tk.Button(sub, text="Cerrar", command=sub.destroy).pack(pady=5)
