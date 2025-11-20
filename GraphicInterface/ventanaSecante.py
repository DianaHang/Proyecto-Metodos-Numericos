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
from Methods.Secante import metodoSecante, f1


def ventanaSecante():
    sub = tk.Toplevel()
    sub.title("Método de la Secante")
    sub.geometry("380x350")

    tk.Label(sub, text="Método de la Secante",
             font=("Arial", 16, "bold")).pack(pady=10)

    tk.Label(sub, text="Valor inicial x0:").pack()
    entrada_x0 = tk.Entry(sub, width=10)
    entrada_x0.pack()

    tk.Label(sub, text="Valor inicial x1:").pack()
    entrada_x1 = tk.Entry(sub, width=10)
    entrada_x1.pack()

    resultado = tk.Label(sub, text="", wraplength=300)
    resultado.pack(pady=10)

    def ejecutar():
        try:
            x0 = float(entrada_x0.get())
            x1 = float(entrada_x1.get())
            df, raiz = metodoSecante(f1, x0, x1, n=10)
            resultado.config(text=f"Raíz aproximada: {raiz:.6f}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(sub, text="Calcular", command=ejecutar).pack(pady=5)
    tk.Button(sub, text="Cerrar", command=sub.destroy).pack()