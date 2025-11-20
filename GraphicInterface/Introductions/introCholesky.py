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

from GraphicInterface.ventanaCholesky import ventanaCholesky 


def introCholesky(root):
    intro = tk.Toplevel(root)
    intro.title("Introducción - Método de Cholesky")
    intro.geometry("500x450")

    texto = (
    "Descomposición de Cholesky\n\n"
    "Este método de factorización se utiliza únicamente para matrices "
    "simétricas y definidas positivas.\n\n"
    "Descompone la matriz A en el producto LLᵀ, donde L es triangular inferior.\n\n"
    "Es más rápido y estable numéricamente que la factorización LU general.\n\n"
    "Haz clic en CONTINUAR para realizar la descomposición de Cholesky."
)

    lbl = tk.Label(intro, text=texto, font=("Arial", 12), justify="left", wraplength=450)
    lbl.pack(pady=20)

    btn_continuar = tk.Button(intro, text="Continuar",
                              font=("Arial", 12),
                              command=lambda: abrirCholesky(intro))
    btn_continuar.pack(pady=5)

    btn_regresar = tk.Button(intro, text="Regresar al menú",
                             font=("Arial", 12),
                             command=intro.destroy)
    btn_regresar.pack(pady=5)


def abrirCholesky(intro):
    intro.destroy()  # Cierra la introducción
    ventanaCholesky() # Abre tu ventana original