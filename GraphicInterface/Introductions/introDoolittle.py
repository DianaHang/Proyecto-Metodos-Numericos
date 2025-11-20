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

from GraphicInterface.ventanaDoolitle import ventanaDoolittle


def introDoolittle(root):
    intro = tk.Toplevel(root)
    intro.title("Introducción - Método de Doolittle")
    intro.geometry("500x450")

    texto = (
    "Factorización LU (Método de Doolittle)\n\n"
    "La factorización LU descompone una matriz A en el producto de una "
    "matriz triangular inferior L y una triangular superior U.\n\n"
    "El método de Doolittle fija la diagonal de L en unos y calcula el resto "
    "de los elementos mediante operaciones sistemáticas.\n\n"
    "Esta técnica permite resolver múltiples sistemas Ax=b de forma muy "
    "eficiente.\n\n"
    "Haz clic en CONTINUAR para aplicar la factorización LU."
)



    lbl = tk.Label(intro, text=texto, font=("Arial", 12), justify="left", wraplength=450)
    lbl.pack(pady=20)

    btn_continuar = tk.Button(intro, text="Continuar",
                              font=("Arial", 12),
                              command=lambda:  abrirDoolittle(intro))
    btn_continuar.pack(pady=5)

    btn_regresar = tk.Button(intro, text="Regresar al menú",
                             font=("Arial", 12),
                             command=intro.destroy)
    btn_regresar.pack(pady=5)


def abrirDoolittle(intro):
    intro.destroy()  # Cierra la introducción
    ventanaDoolittle()  # Abre tu ventana original