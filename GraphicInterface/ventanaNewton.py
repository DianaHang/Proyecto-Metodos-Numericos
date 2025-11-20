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
from Methods.Newton import metodoNewton, funcion1, derivf1


def ventanaNewton():
    sub = tk.Toplevel()
    sub.title("Método de Newton")
    sub.geometry("380x350")

    tk.Label(sub, text="Método de Newton",
             font=("Arial", 16, "bold")).pack(pady=10)

    tk.Label(sub, text="Valor inicial x0:").pack()
    entrada_x0 = tk.Entry(sub, width=10)
    entrada_x0.pack()

    resultado = tk.Label(sub, text="", wraplength=300)
    resultado.pack(pady=10)

    def ejecutar():
        try:
            x0 = float(entrada_x0.get())
            df, raiz = metodoNewton(funcion1, derivf1, x0, n=10)
            resultado.config(text=f"Raíz aproximada: {raiz:.6f}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(sub, text="Calcular", command=ejecutar).pack(pady=5)
    tk.Button(sub, text="Cerrar", command=sub.destroy).pack()
