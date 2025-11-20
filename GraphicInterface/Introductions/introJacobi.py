import sys
import os
### Ajustar ruta para importar módulos del proyecto
ruta_actual = os.path.dirname(os.path.abspath(__file__))          # /GraphicInterface
ruta_proyecto = os.path.dirname(ruta_actual)                      # /ProyectoFinal

if ruta_proyecto not in sys.path:
    sys.path.insert(0, ruta_proyecto)

"""##################################################
"""
#Librerías
import tkinter as tk
from tkinter import messagebox

from GraphicInterface.ventanaJacobi import ventanaJacobi


def introJacobi(root):
    intro = tk.Toplevel(root)
    intro.title("Introducción - Método de Jacobi")
    intro.geometry("500x450")

    texto = (
    "Método Iterativo de Jacobi\n\n"
    "Este método resuelve sistemas de ecuaciones lineales de forma iterativa, "
    "usando aproximaciones sucesivas.\n\n"
    "Cada variable se despeja de su ecuación correspondiente y se evalúa "
    "utilizando los valores de la iteración anterior.\n\n"
    "La convergencia está garantizada si la matriz es diagonalmente dominante "
    "o simétrica definida positiva.\n\n"
    "Haz clic en CONTINUAR para utilizar el método de Jacobi."
)


    lbl = tk.Label(intro, text=texto, font=("Arial", 12), justify="left", wraplength=450)
    lbl.pack(pady=20)

    btn_continuar = tk.Button(intro, text="Continuar",
                              font=("Arial", 12),
                              command=lambda: abrirJacobi(intro))
    btn_continuar.pack(pady=5)

    btn_regresar = tk.Button(intro, text="Regresar al menú",
                             font=("Arial", 12),
                             command=intro.destroy)
    btn_regresar.pack(pady=5)


def abrirJacobi(intro):
    intro.destroy()  # Cierra la introducción
    ventanaJacobi()  # Abre tu ventana original